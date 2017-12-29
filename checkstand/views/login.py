from django.shortcuts import render, redirect, HttpResponse
from checkstand.models import Seller


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
    if request.method == 'POST':
        message = "请检查填写的内容！"
        sellername = request.POST.get('username')
        password = request.POST.get('password')
        try:
            seller = Seller.objects.get(name=sellername)
            if seller.password == password:
                request.session['is_login'] = True
                request.session['seller_id'] = seller.id
                request.session['seller_name'] = seller.name
                return redirect('/checkstand/home/')
            else:
                message = "密码不正确！"
        except:
            message = "用户不存在！"
        return render(request, 'checkstand/login.html', locals())


def logout(request):
    if not request.session.get('is_login', False):
        return redirect('/checkstand/home/')
    request.session.flush()
    return redirect('/checkstand/loginpage')
