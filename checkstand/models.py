from django.db import models

# Create your models here.

class Kind(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Menu(models.Model):
    kind = models.ForeignKey(Kind)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    img=models.ImageField(upload_to='images')
    def __str__(self):
        return self.name

