from django.conf.urls import url
from checkstand.views import home, historyorders, managemenu, managedesk, income,analyze

urlpatterns = [

    # 收银台
    url(r'^home/$', home.index, name='home'),
    url(r'^paybill/$', home.pay_bill, name='pay_bill'),
    url(r'^showorderdetal/$', home.show_order_detal, name='show_order_detal'),
    # 历史订单
    url(r'^history/page=(?P<page>\d+)$', historyorders.paging, name='page'),

    # ---管理功能----
    # 桌号
    url(r'^managedesk/$', managedesk.index, name='manage_desk'),
    url(r'^deskaddmany/$', managedesk.add_many, name='desk_add_many'),
    url(r'^deskdelsingle/$', managedesk.del_single, name='desk_del_single'),
    # 菜类
    url(r'^managekind/$', managemenu.kind_index, name='manage_kind'),

    url(r'^actionkindcreate/$', managemenu.add_kind_action, name='action_kind_create'),
    url(r'^actionkindupdate/$', managemenu.update_kind_action, name='action_kind_update'),
    url(r'^actionkinddelete/$', managemenu.delete_kind_action, name='action_kind_delete'),
    # 菜品
    url(r'^menumanage/$', managemenu.index, name='manage_menu'),

    url(r'^actionmenucreate/$', managemenu.create_menu_action, name='action_menu_create'),
    url(r'^actionmenuupdate/$', managemenu.update_menu_action, name='action_menu_update'),
    url(r'^actionmenudelete/$', managemenu.delete_menu_action, name='action_menu_delete'),

    # ----收入----
    url(r'^incomeday/$', income.day, name='income_day'),
    url(r'^incomemonth/$', income.month, name='income_month'),
    url(r'^incomeyear/$', income.year, name='income_year'),

    url(r'^ajaxincomeday/$', income.ajax_day, name='ajax_income_day'),
    url(r'^ajaxincomemonth/$', income.ajax_month, name='ajax_income_month'),
    # ----分析----
    url(r'^analyzeorder/$', analyze.order, name='analyze_order'),
    url(r'^analyzeormenu/$', analyze.menu, name='analyze_menu'),

]
