from django.db import models


class Kind(models.Model):
    name = models.CharField(max_length=20)
    state = models.BooleanField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    kind = models.ForeignKey(Kind)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
    img = models.ImageField(upload_to='menus')
    state = models.BooleanField()

    def __str__(self):
        return self.name


class Desk(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False)
    qr_coder = models.ImageField(upload_to="desks")
    state = models.BooleanField()

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    desk = models.ForeignKey('Desk')
    time = models.DateTimeField(auto_now_add=True)
    remark = models.CharField(max_length=200)
    totle_price = models.IntegerField()
    state = models.BooleanField()

    def __str__(self):
        return str(self.time)


class OrderDetail(models.Model):
    order = models.ForeignKey('Order')
    menu = models.ForeignKey('Menu')
    num = models.IntegerField()


class Seller(models.Model):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=10, choices=gender, default='男')
    create_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-create_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
