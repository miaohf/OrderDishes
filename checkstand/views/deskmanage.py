from django.shortcuts import render
from order.models import Desk


def index(request):
    desks = Desk.objects.all()
    return render(request, 'checkstand/deskmanage.html', locals())
