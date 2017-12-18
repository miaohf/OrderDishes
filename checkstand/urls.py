from django.conf.urls import url
from checkstand.views import home, historyorders, menumanage, deskmanage, income

urlpatterns = [

    # 收银台
    url(r'^home/$', home.index, name='home'),
    url(r'^payaction/$', home.pay_action, name='payaction'),

    # 历史订单
    url(r'^history/page=(?P<page>\d+)$', historyorders.paging, name='page'),

    # ---管理功能----
    # 桌号
    url(r'^deskmanage/$', deskmanage.index, name='deskmanage'),

    # 菜类
    url(r'^menukindmanage/$', menumanage.kindindex, name='menukindmanage'),

    url(r'^addkindacion/$', menumanage.add_kind_action, name='addkindaction'),
    url(r'^updatekindacion/$', menumanage.update_kind_action, name='updatekindacion'),
    url(r'^deletekindacion/$', menumanage.delete_kind_action, name='deletekindacion'),
    # 菜品
    url(r'^menumanage/$', menumanage.index, name='menumanage'),

    url(r'^createmenuaction/$', menumanage.create_menu_action, name='createaction'),
    url(r'^updatamenuacion/$', menumanage.update_menu_action, name='updateaction'),
    url(r'^deletemenuacion/$', menumanage.delete_menu_action, name='deleteaction'),

    # ----收入----
    url(r'^incomeday/$', income.day, name='incomeday'),
    url(r'^incomemonth/$', income.month, name='incomemonth'),
    url(r'^incomeyear/$', income.year, name='incomeyear'),

    url(r'^dayincomeajax/$', income.ajaxday, name='dayincomajax'),
    url(r'^monthincomeajax/$', income.ajaxmonth, name='monthincomajax'),
    # url(r'test/$', home.test, name='test'),
]
