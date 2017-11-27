from django.db import models
# Create your models here.

class Desk(models.Model):
    id=models.AutoField(auto_created=True, primary_key=True, serialize=False)
class Order(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    desk_id = models.ForeignKey(Desk)
    time = models.DateTimeField(auto_created=True)
    remark = models.CharField(max_length=200)
    def __str__(self):
        return self.id
