from django.contrib import admin
from order.models import Order,Desk
# Register your models here.
admin.site.register(Desk)
admin.site.register(Order)