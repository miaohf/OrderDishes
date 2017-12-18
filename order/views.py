from django.shortcuts import render
from checkstand.models import Menu,Kind
from order.models import Order,Order_details
# Create your views here.
def index(request):
    kinds=Kind.objects.all()
    menus= Menu.objects.all()
    return render(request,'order/index.html',{'kinds':kinds,'menus':menus})

def order_aciton(request):
    if request.method=="POST":
        checkbox_list=request.POST.getlist('checkbox_list')
        desk=request.POST.get('desk_id')
        totleprice = 0
        for menu_id in checkbox_list:
            totleprice+=Menu.objects.get(id=menu_id).price
        order_id=Order.objects.create(desk_id=int(desk), remark='kkk',totle_price=totleprice,state=0).id
        for checkbox in checkbox_list:
            Order_details.objects.create(num=1,menu_id=int(checkbox),order_id=int(order_id))
    return render(request,'order/success.html')