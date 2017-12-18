from django.shortcuts import render
from order.models import Order, Order_details


def index(request):
    orders = Order.objects.all()
    order_details = Order_details.objects.all()
    return render(request, 'checkstand/homepage.html', locals())


def pay_action(request):
    order_id = request.POST.get('order_id')
    Order.objects.filter(id=order_id).update(state=True)
    orders = Order.objects.all()
    order_details = Order_details.objects.all()
    return render(request, 'checkstand/homepage.html', locals())
