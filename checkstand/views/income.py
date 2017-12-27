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
    return render(request, 'checkstand/incomeyear.html')


"""
    功能：查询这一天的订单，计算每个菜相应收入，每个菜的销量，每个菜类的销量
    传入：时间(年-月-日)
    正确返回：成功状态，当天所有订单，(今日菜品销量，今日菜类销量，今日菜品收入)都是{key='name':value='nuber'}
    错误返回：没有这一天，
    
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
    # 对菜品销量排序
    menu_sales = dict(sorted(menu_sales.items(), key=lambda x: x[1], reverse=True))
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
    功能：查询月订单，且计算本月有多少天
    传入：时间（年—月）
    正确返回：成功状态，这个月的所有订单，本月多少天
    错误返回：空状态，本月有多少天
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


"""
    功能：计算每个月的收入和年收入
    传入：年份
    正确返回：成功状态，一年中每个月的收入（list），年收入
    错误返回：为空状态，一年中每个月的收入（list都为0），年收入为0
"""


def ajax_year(request):
    year = request.POST['time']
    income_year = []
    total_income_year = 0
    if (Order.objects.filter(time__year=year, state=True)):
        for month in range(1, 13):
            income_month = 0
            month_orders = Order.objects.filter(time__year=year, time__month=month, state=True)
            for month_order in month_orders:
                income_month += month_order.totle_price
            income_year.append(income_month)
            total_income_year += income_month
        response_data = {'state': 'success', 'income_year': income_year, 'total_income_year': total_income_year}
    else:
        response_data = {'state': 'null', 'income_year': income_year, 'total_income_year': total_income_year}
    return HttpResponse(JsonResponse(response_data), content_type="application/json")
