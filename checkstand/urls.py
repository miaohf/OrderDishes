from django.conf.urls import url
from checkstand.views import update_menu

urlpatterns = [
    url(r'^index/$', update_menu.index, name='index'),
    url(r'^historyorders/$', update_menu.hostory, name='history'),
    url(r'^updatamenu/$', update_menu.updata_menu, name='updata'),

    url(r'^addkindacion/$', update_menu.add_kind_action, name='addkindaction'),
    url(r'^updatekindacion/$', update_menu.update_kind_action, name='updatekindacion'),
    url(r'^deletekindacion/$', update_menu.delete_kind_action, name='deletekindacion'),

    url(r'^createmenuaction/$', update_menu.create_menu_action, name='createaction'),
    url(r'^updatamenuacion/$', update_menu.update_menu_action, name='updateaction'),
    url(r'^deletemenuacion/$', update_menu.delete_menu_action, name='deleteaction'),



    url(r'^queryajx/$',update_menu.query_ajax,name='queryajx')
]
