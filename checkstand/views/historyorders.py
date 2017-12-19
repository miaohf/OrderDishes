from django.shortcuts import render
from order.models import Order, Order_details
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404


def paging(request, page):
    try:
        currentpage = int(page)
    except ValueError:
        raise Http404()
    orders_list = Order.objects.filter(state=True).order_by('-id')
    order_details = Order_details.objects.all()
    paginator = Paginator(orders_list, 15)
    try:
        orders = paginator.page(currentpage)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    return render(request, 'checkstand/history_orders.html', locals())
