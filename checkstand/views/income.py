from django.shortcuts import render
from django.http import HttpResponse
from checkstand.models import Order, OrderDetail
from django.http import JsonResponse
from django.core import serializers
import json
import re
import calendar


def day(request):
    return render(request, 'checkstand/incomeday.html')


def month(request):
    return render(request, 'checkstand/incomemonth.html')


def year(request):
    return render(request, 'checkstand/incomeday.html')


""""
    如果查询到这一天的订单,则处理得到：
        每个菜相应收入
        每个菜的销量
        每个菜类的销量
        返回
    没有查询到：
        返回没有找到
"""


def ajax_day(request):
    menu_sales = {}
    menu_income = {}
    menu_kind = {}
    times = re.split(r"-", request.POST['time'])
    orders = Order.objects.filter(time__year=times[0], time__month=times[1], time__day=times[2], state=True)
    for order in orders:
        order_details = OrderDetail.objects.filter(order=order)
        for order_detail in order_details:
            if order_detail.menu.name in menu_sales:
                menu_sales[order_detail.menu.name] += order_detail.num
                menu_income[order_detail.menu.name] += order_detail.menu.price
            else:
                menu_sales[order_detail.menu.name] = order_detail.num
                menu_income[order_detail.menu.name] = order_detail.menu.price
            if order_detail.menu.kind.name in menu_kind:
                menu_kind[order_detail.menu.kind.name] += order_detail.num
            else:
                menu_kind[order_detail.menu.kind.name] = order_detail.num
    if orders:
        response_data = {
            'state': "success",
            'orders': serializers.serialize('json', orders),
            'menuSales': json.dumps(menu_sales, ensure_ascii=False),
            'menuIncome': json.dumps(menu_income, ensure_ascii=False),
            'menuKind': json.dumps(menu_kind, ensure_ascii=False),
        }
    else:
        response_data = {'state': 'noday'}
    return HttpResponse(JsonResponse(response_data), content_type="application/json")


"""
    如果查询到这月的订单,则处理得到：
        当月的订单
        当月有多少天
        返回
    没有查询到：
        返回为空
"""


def ajax_month(request):
    time = request.POST['time']
    times = re.split('-', time)
    days = calendar.monthrange(int(times[0]), int(times[1]))[1]
    income_month = Order.objects.filter(time__year=times[0], time__month=times[1], state=True)
    if income_month:
        response_data = {'state': 'success',
                         'orderMonth': serializers.serialize('json', income_month),
                         'days': days}
    else:
        response_data = {'state': 'null', 'days': days}
    return HttpResponse(JsonResponse(response_data), content_type="application/json")
