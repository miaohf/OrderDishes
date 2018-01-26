from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^desk=(?P<id>\d+)$', views.index),
    url(r'^orderaciton', views.order_aciton, name="orderaciton"),
    url(r'^placeorder/$', views.place_order, name='place_order')
]
