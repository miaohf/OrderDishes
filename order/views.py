from django.shortcuts import render
from checkstand.models import Menu, Kind, Desk
from checkstand.models import Order, OrderDetail


# Create your views here.
def index(request, id):
    desk_id = Desk.objects.get(id=id, state=True).id
    kinds = Kind.objects.filter(state=True)
    menus = Menu.objects.filter(state=True)
    return render(request, 'order/index.html', locals())


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
