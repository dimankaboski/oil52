from django.shortcuts import render
from django.http import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string, get_template
from django.shortcuts import render_to_response
from django.core import serializers
from decimal import Decimal
from django.core.mail import EmailMessage
from django.template import Context


import base64
from django.core.files.base import ContentFile
#check


def index(request):
    goods = Good.objects.filter(cat='Oil')[:5]
    goods_trans = Good.objects.filter(cat='transmission')[:5]
    return render(request, 'index.html', {'goods': goods, 'goods_trans':goods_trans})


def motoroil(request):

    return render(request, 'motoroil.html')

def deliver(request):

    return render(request, 'deliver.html')


def transmission(request):

    return render(request, 'transmission.html')


def mototechnic(request):

    return render(request, 'mototechnic.html')


def technical_liquid(request):

    return render(request, 'technical_liquid.html')


def lubricants(request):

    return render(request, 'lubricants.html')


def email(request):

    return render(request, 'email.html')


def order(request):
    subject = "Hello test"
    from_email = 'service.automasla52@yandex.ru'
    if request.method == 'POST':
        order = Orders.objects.create()
        order.firstname = request.POST['firstname']
        order.lastname = request.POST['lastname']
        order.phone = request.POST['phone']
        order.mail = request.POST['email']
        order.adress = request.POST['adress']
        order.description = request.POST['description']
        if request.POST['Radiobut'] == 'option1':
            order.payment = 'Off'
        if request.POST['Radiobut'] == 'option2':
            order.payment = 'On'
        order.save()
        lastorder = Orders.objects.last()
        cart_sum = 0
        to = []
        to.append(order.mail)
        cart_goods = list(Good.objects.filter(id__in=request.session['cart'].keys()).values('id', 'name', 'cost','volume'))
        for g in cart_goods:
            g['count'] = request.session['cart'][str(g['id'])]
            cart_sum = cart_sum + int(g['cost']) * int(g['count'])
        ctx = {
            'order': lastorder,
            'cart_sum':cart_sum,
            'cart_goods':cart_goods,
        }
        message = get_template('email.html').render(ctx)
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = 'html'
        msg.send()
    return render(request, 'order.html')


def motoroil_good(request, motoroil_id):
    good = Good.objects.filter(id=motoroil_id)
    alsogoodname = [p.name for p in good]
    test = ['Technical','Lubricants']
    alsogood = Good.objects.filter(name__icontains=alsogoodname[0])
    othergoods = Good.objects.filter(cat__in=test).order_by('?')[:5]
    return render(request, 'motoroil_good.html', {'good': good, 'alsogood': alsogood, 'othergoods': othergoods})


@csrf_exempt
def getgoods(request, cat):
    if cat == 'oil':
        goods = list(Good.objects.filter(cat = 'Oil').values('id', 'name', 'cost', 'description', 'viscosity', 'type', 'volume', 'img'))
    elif cat == 'transmission':
        goods = list(Good.objects.filter(cat = 'transmission').values('id', 'name', 'cost', 'description', 'viscosity', 'type', 'volume', 'img'))
    elif cat == 'Mototechnic':
        goods = list(Good.objects.filter(cat = 'Mototechnic').values('id', 'name', 'cost', 'description', 'viscosity', 'type', 'volume', 'img'))
    elif cat == 'Technical':
        goods = list(Good.objects.filter(cat = 'Technical').values('id', 'name', 'cost', 'description', 'volume', 'img', 'tec_category'))
    elif cat == 'Lubricants':
        goods = list(Good.objects.filter(cat = 'Lubricants').values('id', 'name', 'cost', 'description', 'volume', 'img'))

    return JsonResponse(goods, safe=False)


def cart(request):

    return render(request, 'cart.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        context = {}
        q = request.GET['q']
        souv = Good.objects.filter(name__icontains=q)
        context['goods'] = souv
        context['query'] = q
        return render_to_response('find.html',
            context)
    else:
        return HttpResponse('Введите слово для поиска.')
    return render(request, 'find.html')


@csrf_exempt
def getcart(request):
    request.session.modified = True
    if 'cart' not in request.session:
        request.session['cart'] = {}
    goods = list(Good.objects.filter(id__in=request.session['cart'].keys()).values('id', 'name', 'cost', 'volume', 'img'))
    for g in goods:
        g['count'] = request.session['cart'][str(g['id'])]
    return JsonResponse(goods, safe=False)


@csrf_exempt
def changecount(request, good_id, good_count):
    request.session.modified = True
    request.session['cart'][str(good_id)] = good_count
    return JsonResponse(request.session['cart'], safe=False)


@csrf_exempt
def getcartinfo(request):
    goods = eval(str(Good.objects.filter(id__in=request.session['cart'].keys()).values(
        'id', 'name', 'cost', 'volume', 'img'))[10:-1])
    return JsonResponse(goods, safe=False)


@csrf_exempt
def gooddelete(request, good_id):
    request.session.modified = True
    request.session['cart'].pop(str(good_id), None)
    return JsonResponse(request.session['cart'], safe=False)


@csrf_exempt
def addtocart(request, good_id):
    count = 1
    request.session.modified = True
    if 'cart' not in request.session:
        request.session['cart'] = {}
    if int(good_id) not in request.session['cart']:
        request.session['cart'][str(good_id)] = count
    else:
        request.session['cart'] = {}
    return JsonResponse(request.session['cart'], safe=False)

def custom404(request):
    return HttpResponse('This is error 404', status=404)