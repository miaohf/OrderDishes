from django.shortcuts import render
from django.http import HttpResponse
from order.models import Order, Order_details
from django.http import JsonResponse
from django.core import serializers
import json
import re


def day(request):
    return render(request, 'checkstand/incomeday.html')


def month(request):
    return render(request, 'checkstand/incomemonth.html')


def year(request):
    return render(request, 'checkstand/incomeday.html')


def ajaxday(request):
    orders = []
    menusales = {}
    menuincome = {}
    time = request.POST['time']
    times = re.split(r"-", time)
    year = int(times[0])
    month = int(times[1])
    day = int(times[2])
    for order in Order.objects.all():
        if order.time.year == year and order.time.month == month and order.time.day == day:
            orders.append(order)
    for order_detail in Order_details.objects.all():
        for order in orders:
            if order.id == order_detail.order_id:
                if order_detail.menu.name in menusales:
                    menusales[order_detail.menu.name] += order_detail.num
                    menuincome[order_detail.menu.name] += order_detail.menu.price
                else:
                    menusales[order_detail.menu.name] = order_detail.num
                    menuincome[order_detail.menu.name] = order_detail.menu.price
    if orders:
        response_data = {
            'state': "success",
            'menusales': json.dumps(menusales, ensure_ascii=False),
            'orders': serializers.serialize('json', orders),
            'menuincome': json.dumps(menuincome, ensure_ascii=False),
        }
        return HttpResponse(JsonResponse(response_data), content_type="application/json")
    else:
        response_data = {
            'state': 'noday',
        }
        return HttpResponse(JsonResponse(response_data), content_type="application/json")


def ajaxmonth(request):
    time = request.POST['time']
    times = re.split('-', time)
    try:
        incomemonth = Order.objects.filter(time__year=times[0], time__month=times[1])
    except BaseException as e:
        print(e)
    response_data = {'state': 'success',
                     'incomemonth': serializers.serialize('json', incomemonth),
                     }
    return HttpResponse(JsonResponse(response_data), content_type="application/json")
