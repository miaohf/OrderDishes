from django.contrib import admin
from order.models import Order,Desk,Order_details
# Register your models here.
admin.site.register(Desk)
admin.site.register(Order)
admin.site.register(Order_details)