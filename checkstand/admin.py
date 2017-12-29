from django.contrib import admin
from checkstand.models import Menu, Desk, Order, OrderDetail,Seller

# Register your models here.
admin.site.register(Seller)
admin.site.register(Menu)
admin.site.register(Desk)
admin.site.register(Order)
admin.site.register(OrderDetail)
