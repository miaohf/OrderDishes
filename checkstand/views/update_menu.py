from django.shortcuts import render
from checkstand.models import Menu,Kind
from django.http import HttpResponse
from order.models import Order
# Create your views here.
# 页面
def index(request):
    return render(request, 'checkstand/index.html')

def hostory(request):
    orders=Order.objects.all
    return render(request,'checkstand/history_orders.html',{'orders':orders})

def updata_menu(request):
    kinds = Kind.objects.all
    menus=Menu.objects.all()
    return render(request, 'checkstand/update_menu.html', {'kinds':kinds,'menus':menus})


# 增删改菜单action
def create_menu_action(request):
    name = request.POST.get('name', 'NAME')  # 如果为空则默认为NAME
    price = request.POST.get('price', 'PRICE')
    kind_name=request.POST.get('kind_name')
    kind=Kind.objects.get(name=kind_name)
    Menu.objects.create(name=name, price=price,kind=kind)
    kinds = Kind.objects.all
    menus = Menu.objects.all()
    return render(request, 'checkstand/update_menu.html', {'kinds': kinds, 'menus': menus})
def update_menu_action(request):
    id=request.POST.get('id')
    name=request.POST.get('name','NAME')
    price=request.POST.get('price','PRICE')
    Menu.objects.filter(id=id).update(name=name,price=price)
    kinds = Kind.objects.all
    menus = Menu.objects.all()
    return render(request, 'checkstand/update_menu.html', {'kinds': kinds, 'menus': menus})
def delete_menu_action(request):
    id=request.POST.get('id')
    Menu.objects.filter(id=id).delete()
    kinds = Kind.objects.all
    menus = Menu.objects.all()
    return render(request, 'checkstand/update_menu.html', {'kinds': kinds, 'menus': menus})


#增删改菜类action
def add_kind_action(request):
    name=request.POST.get('kind_name')
    Kind.objects.create(name=name)
    kinds = Kind.objects.all
    menus = Menu.objects.all()
    return render(request, 'checkstand/update_menu.html', {'kinds': kinds, 'menus': menus})

def delete_kind_action(request):
    name=request.POST.get('kind_name')
    Kind.objects.filter(name=name).delete()
    # kind=Kind.objects.get(name=name)
    # Menu.objects.filter(kind=kind).delete()
    # Kind.objects.filter(name=name).delete()
    kinds = Kind.objects.all
    menus = Menu.objects.all()
    return render(request, 'checkstand/update_menu.html', {'kinds': kinds, 'menus': menus})

def update_kind_action(request):
    oldname=request.POST.get('oldkindname')
    newname=request.POST.get('newkindname')
    Kind.objects.filter(name=oldname).update(name=newname)
    kinds = Kind.objects.all
    menus = Menu.objects.all()
    return render(request, 'checkstand/update_menu.html', {'kinds': kinds, 'menus': menus})


def query_ajax(request):
    name=request.POST.get('username')
    Menu.objects.get(name=name)
    return HttpResponse('success')

