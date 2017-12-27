from django.shortcuts import render
from checkstand.models import Order, OrderDetail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, Http404


def paging(request, page):
    try:
        currentpage = int(page)
    except ValueError:
        raise Http404()
    orders_list = Order.objects.order_by('-id')
    order_details = OrderDetail.objects.all()
    paginator = Paginator(orders_list, 11)
    try:
        orders = paginator.page(currentpage)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)

    return render(request, 'checkstand/historyorders.html', locals())
