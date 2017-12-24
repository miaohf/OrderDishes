from django.conf.urls import url
from checkstand.views import home, historyorders, menumanage, deskmanage, income

urlpatterns = [

    # 收银台
    url(r'^home/$', home.index, name='home'),
    url(r'^paybill/$', home.pay_bill, name='pay_bill'),
    url(r'^showorderdetal/$', home.show_order_detal, name='show_order_detal'),
    # 历史订单
    url(r'^history/page=(?P<page>\d+)$', historyorders.paging, name='page'),

    # ---管理功能----
    # 桌号
    url(r'^deskmanage/$', deskmanage.index, name='deskmanage'),
    url(r'^deskaddmany/$', deskmanage.add_many, name='desk_add_many'),
    url(r'^deskdelsingle/$', deskmanage.del_single, name='desk_del_single'),
    # 菜类
    url(r'^menukindmanage/$', menumanage.kind_index, name='menukindmanage'),

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

    url(r'^dayincomeajax/$', income.ajax_day, name='dayincomajax'),
    url(r'^monthincomeajax/$', income.ajax_month, name='monthincomajax'),
    # url(r'test/$', home.test, name='test'),
]
