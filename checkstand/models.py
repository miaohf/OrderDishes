from django.db import models
from order.models import Order
# Create your models here.

class Kind(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Menu(models.Model):
    kind = models.ForeignKey(Kind)
    name = models.CharField(max_length=30)
    price = models.IntegerField(max_length=3)
    def __str__(self):
        return self.name

