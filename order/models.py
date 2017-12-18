from django.db import models
from checkstand.models import Menu


# Create your models here.

class Desk(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)


class Order(models.Model):
    desk = models.ForeignKey(to='Desk', to_field='id')
    time = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=200)
    totle_price = models.IntegerField()
    state = models.BooleanField()


class Order_details(models.Model):
    order = models.ForeignKey('Order')
    menu = models.ForeignKey('checkstand.Menu')
    num = models.IntegerField()
