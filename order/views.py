from django.shortcuts import render
from checkstand.models import Menu, Kind, Desk
from checkstand.models import Order, OrderDetail
from django.http import JsonResponse
import json


# Create your views here.
def index(request, id):
    desk_id = Desk.objects.get(id=id, state=True).id
    kinds = Kind.objects.filter(state=True)
    menus = Menu.objects.filter(state=True)
    return render(request, 'order/orderpage.html', locals())


def order_aciton(request):
    if request.method == "POST":
        checkbox_list = request.POST.getlist('checkbox_list')
        desk = request.POST.get('desk_id')
        totleprice = 0
        for menu_id in checkbox_list:
            totleprice += Menu.objects.get(id=menu_id).price
        order_id = Order.objects.create(desk_id=int(desk), remark='kkk', totle_price=totleprice, state=0).id
        for checkbox in checkbox_list:
            OrderDetail.objects.create(num=1, menu_id=int(checkbox), order_id=int(order_id))
    return render(request, 'order/success.html')


def place_order(request):
    if request.method == 'POST':
        desk_id = request.POST.get('desk_id')
        try:
            Order.objects.get(desk_id=desk_id, state=False)
            return JsonResponse({'state': 'ordered'})
        except Order.DoesNotExist:
            order_menus = json.loads(request.POST.get('order_menu'))
            remark = request.POST.get('remark')
            totleprice = 0
            for menu_id in order_menus:
                totleprice += Menu.objects.get(id=menu_id).price * order_menus[menu_id]
            order_id = Order.objects.create(desk_id=int(desk_id), remark=remark, totle_price=totleprice, state=0).id
            for order_menu_id in order_menus:
                OrderDetail.objects.create(num=int(order_menus[order_menu_id]), menu_id=int(order_menu_id),
                                           order_id=int(order_id))
            return JsonResponse({'state': 'success'})
