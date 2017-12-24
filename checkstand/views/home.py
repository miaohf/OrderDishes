from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from checkstand.models import Order, OrderDetail, Menu
from django.core import serializers
import json
import re


def index(request):
    orders = Order.objects.filter(state=False)
    order_details = OrderDetail.objects.all()
    return render(request, 'checkstand/homepage.html', locals())


def show_order_detal(request):
    bills = []
    order_details = OrderDetail.objects.filter(order_id=request.POST.get("orderId"))
    for menu in Menu.objects.all():
        for order_detail in order_details:
            if menu.id is order_detail.menu.id:
                bills.append({'menu_name': menu.name,
                              'order_num': order_detail.num,
                              'menu_price': menu.price,
                              'totle_price': order_detail.num * menu.price,
                              })
    response_data = {
        'state': 'success',
        'bills': json.dumps(bills, ensure_ascii=False),
    }
    return HttpResponse(JsonResponse(response_data))


def pay_bill(request):
    order_id = re.split(r'：', request.POST.get('orderId'))
    id = order_id[1]
    Order.objects.filter(id=id).update(state=True)
    response_data = {
        'state': 'success',
        'order_id': id,
    }
    return HttpResponse(JsonResponse(response_data))
