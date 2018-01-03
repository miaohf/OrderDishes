from django.shortcuts import render, redirect
from django.http import JsonResponse
from checkstand.models import Seller
from django.urls import reverse
from datetime import datetime
from django.conf import settings
import os


def login_index(request):
    return render(request, 'checkstand/login.html')


# def login(request):
#     if request.method == "POST":
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)
#         if username and password:  # 确保用户名和密码都不为空
#             username = username.strip()
#             # 用户名字符合法性验证
#             # 密码长度验证
#             # 更多的其它验证.....
#             try:
#                 user = Seller.objects.get(name=username)
#             except:
#                 return HttpResponse('没有这个帐号')
#             if user.password == password:
#                 return redirect('/checkstand/home/')
#     message = '密码错误，请重新输入！'
#     return render(request, 'checkstand/login.html', locals())

def login(request):
    if request.session.get('is_login', False):
        return redirect('/checkstand/home/')

    return render(request, 'checkstand/login.html', locals())

    # request.META.get('HTTP_REFERER', '/')


def login_ajax(request):
    if request.method == 'POST':

        sellername = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        remember_password = request.POST.get('remember', False)
        print(sellername)
        try:
            seller = Seller.objects.get(email=sellername)
            if seller.password == password:
                Seller.objects.filter(name=seller.name).update(last_login=datetime.now())
                request.session['is_login'] = True
                request.session['seller_id'] = seller.id
                request.session['seller_name'] = seller.name
                request.session['seller_head'] = seller.head.name
                if remember_password != 'true':
                    request.session.set_expiry(0)
                response_data = {'state': 'success', 'url': reverse('checkstand:home')}
                return JsonResponse(response_data)
            else:
                message = "密码不正确！"
        except Seller.DoesNotExist:
            message = "用户不存在！"
        response_data = {'state': 'fail', 'message': message}
        return JsonResponse(response_data)


def logout(request):
    if not request.session.get('is_login', False):
        return redirect('/checkstand/home/')
    request.session.flush()
    return redirect('/checkstand/login/')


def info_index(request):
    id = request.session.get('seller_id')
    seller = Seller.objects.get(id=id)
    seller.password = ''
    return render(request, 'checkstand/personalinfo.html', {'seller': seller})


def info_update(request):
    id = request.session.get('seller_id')
    seller = Seller.objects.get(id=id)
    seller.password = ''
    return render(request, 'checkstand/personalupdate.html', {'seller': seller})


def info_update_ajax(request):
    if request.method == "POST":
        id = request.session.get('seller_id')
        email = request.POST.get('email')
        name = request.POST.get('name')
        sex = request.POST.get('sex')
        try:
            head = request.FILES.get('head')
            path = os.path.join(settings.MEDIA_ROOT, 'head', head.name)
            print(path)
            with open(path, 'wb') as pic:
                for p in head.chunks():
                    pic.write(p)
            print('head/%s' % head.name)
            Seller.objects.filter(id=id).update(name=name, email=email, sex=sex, head='head/%s' % head.name)
        except AttributeError:
            Seller.objects.filter(id=id).update(name=name, email=email, sex=sex)
    seller = Seller.objects.get(id=id)
    request.session['seller_name'] = seller.name
    request.session['seller_head'] = seller.head.name
    return JsonResponse({'name': seller.name, 'email': seller.email, 'sex': seller.sex, 'head': seller.head.name})


def passwd_update(request):
    return render(request, 'checkstand/passwdupdate.html')


def passwd_update_ajax(request):
    id = request.session.get('seller_id')
    old_passwd = request.POST.get('old_passwd')
    new_passwd = request.POST.get('new_passwd')
    seller = Seller.objects.get(id=id)
    if (old_passwd == seller.password):
        Seller.objects.filter(id=id).update(password=new_passwd)
        response_data = {'state': 'success'}
    else:
        response_data = {'state': 'fail'}
    return JsonResponse(response_data)
