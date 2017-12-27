from django.shortcuts import render
from checkstand.models import OrderDetail, Order, Kind, Menu

""""
    模版渲染
    得到：
        所有菜类的{'菜类名',菜类销量}
        所有菜类每个星期的销量{'菜类名',{0:0,1:0....6:0}}（包含没卖出去的菜类）
        所有菜品的菜品销量
"""


def menu(request):
    menu_kinds = {}
    menu_kind_week = {}
    menus = {}
    menu_all = 0
    # 生成菜类的{'菜类名',0},{'菜类名',{0:0,1:0....6:0}}
    for kind in Kind.objects.all():
        week = {}
        for i in range(0, 7):
            week[i] = 0
        menu_kinds[kind.name] = 0
        menu_kind_week[kind.name] = week
    # 生成菜品的字典{'菜品名':0}
    for menu in Menu.objects.all():
        menus[menu.name] = 0
    # 插入数据
    for order_detail in OrderDetail.objects.all():
        kind_name = order_detail.menu.kind.name
        menu_name = order_detail.menu.name
        num = order_detail.num
        weekday = order_detail.order.time.weekday()
        menu_all += order_detail.num
        if kind_name in menu_kinds:
            menu_kinds[kind_name] += num
            menu_kind_week[kind_name][weekday] += num

        if menu_name in menus:
            menus[menu_name] += num
    # 对菜品按value排序,再由list转换dict
    menus = dict(sorted(menus.items(), key=lambda x: x[1], reverse=True))
    return render(request, 'checkstand/analyzemenu.html', locals())
