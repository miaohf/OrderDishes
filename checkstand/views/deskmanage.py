from django.shortcuts import render
from checkstand.models import Desk
from django.conf import settings
from django.http import JsonResponse
from django.core import serializers
import qrcode
import os


def index(request):
    desks = Desk.objects.filter(state=True)
    return render(request, 'checkstand/managedesk.html', locals())


def add_many(request):
    domain = request.POST.get('domain')
    prot = request.POST.get('prot')
    number = request.POST.get('number')
    start = Desk.objects.count() + 1
    end = start + int(number)
    for i in range(start, end):
        url = 'http://{domain}:{prot}/order/desk={desk_id}'.format(domain=domain, prot=prot, desk_id=i)
        img_name = "desk_" + str(i) + ".jpg"
        path = os.path.join(settings.MEDIA_ROOT, 'desks', img_name)
        img = qrcode.make(url)
        img.save(path)
        Desk.objects.create(id=i, qr_coder='/media/desks/%s' % (img_name), state=True)
    desks = Desk.objects.filter(state=True)
    return JsonResponse({
        'state': 'success',
        'start': start,
        'end': end - 1,
        'desks': serializers.serialize('json', desks),
    })


def del_single(request):
    id = request.POST.get('del_id')
    Desk.objects.filter(id=id).update(state=False)
    desks = Desk.objects.filter(state=True)
    return JsonResponse({
        'state': 'success',
        'desks': serializers.serialize('json', desks),
    })
