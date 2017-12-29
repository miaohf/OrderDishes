from django.shortcuts import render
from checkstand.models import Desk
from django.conf import settings
from django.http import JsonResponse,HttpResponse
from django.core import serializers
import qrcode
import os


def index(request):
    desks = Desk.objects.filter(state=True)
    return render(request, 'checkstand/managedesk.html', locals())


"""
    功能：添加多个桌号，生成桌号对应的下单网址，并生成相应二维码
    传入：域名，端口号，数量
    返回：状态，开始桌号，结束桌号，所有存在的桌子对象
"""


def add_many(request):
    domain = request.POST.get('domain')
    prot = request.POST.get('port')
    number = request.POST.get('number')
    start = Desk.objects.count() + 1
    end = start + int(number)
    for i in range(start, end):
        url = 'http://{domain}:{prot}/order/desk={desk_id}'.format(domain=domain, prot=prot, desk_id=i)
        print(url)
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


"""
    功能：删除一张桌子（只是改变了桌子的状态state=false）
    传入：桌子的id号
    返回：所有存在的桌子
"""


def del_single(request):
    id = request.POST.get('del_id')
    Desk.objects.filter(id=id).update(state=False)
    desks = Desk.objects.filter(state=True)
    return JsonResponse({
        'state': 'success',
        'desks': serializers.serialize('json', desks),
    })
