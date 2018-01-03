from django.conf.urls import url
from checkstand.views import home, history_orders, manage_menu, manage_desk, income, analyze, login
from django.contrib.auth import views as auth_view

urlpatterns = [

    # ---收银台----
    url(r'^home/$', home.index, name='home'),
    url(r'^paybill/$', home.pay_bill, name='pay_bill'),
    url(r'^showorderdetal/$', home.show_order_detal, name='show_order_detal'),
    # ---历史订单----
    url(r'^history/page=(?P<page>\d+)$', history_orders.paging, name='page'),

    # ---管理功能----
    # --桌号--
    url(r'^managedesk/$', manage_desk.index, name='manage_desk'),
    url(r'^deskaddmany/$', manage_desk.add_many, name='desk_add_many'),
    url(r'^deskdelsingle/$', manage_desk.del_single, name='desk_del_single'),
    # --菜类--
    url(r'^managekind/$', manage_menu.kind_index, name='manage_kind'),

    url(r'^actionkindcreate/$', manage_menu.add_kind_action, name='action_kind_create'),
    url(r'^actionkindupdate/$', manage_menu.update_kind_action, name='action_kind_update'),
    url(r'^actionkinddelete/$', manage_menu.delete_kind_action, name='action_kind_delete'),
    # --菜品--
    url(r'^menumanage/$', manage_menu.index, name='manage_menu'),

    url(r'^actionmenucreate/$', manage_menu.create_menu_action, name='action_menu_create'),
    url(r'^actionmenuupdate/$', manage_menu.update_menu_action, name='action_menu_update'),
    url(r'^actionmenudelete/$', manage_menu.delete_menu_action, name='action_menu_delete'),

    # ----收入----
    url(r'^incomeday/$', income.day, name='income_day'),
    url(r'^incomemonth/$', income.month, name='income_month'),
    url(r'^incomeyear/$', income.year, name='income_year'),

    url(r'^ajaxincomeday/$', income.ajax_day, name='ajax_income_day'),
    url(r'^ajaxincomemonth/$', income.ajax_month, name='ajax_income_month'),
    url(r'^ajaxincomeyear/$', income.ajax_year, name='ajax_income_year'),
    # ----分析----

    url(r'^analyzeormenu/$', analyze.menu, name='analyze_menu'),

    # 登陆
    url(r'^login/$', login.login, name='login'),
    url(r'^logout/$', login.logout, name='logout'),
    url(r'^loginajax/$', login.login_ajax, name='login_ajax'),
    url(r'^info/$', login.info_index, name='info'),
    url(r'^infoupdate/$', login.info_update, name='info_update'),
    url(r'^infoupdateajax/$', login.info_update_ajax, name='info_update_ajax'),
    url(r'^passwdupdate/$', login.passwd_update, name='passwd_update'),
    url(r'^passwdupdateajax/$', login.passwd_update_ajax, name='passwd_update_ajax'),
]
