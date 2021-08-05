from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from cms.datetime import WhatYear
from price.models import PriceCard, PriceTable, ProductCard
from telebot.sendmessage import sendTelegram

# Create your views here.


def first_page(request):
    slider_list = CmsSlider.objects.all()
    products_card = ProductCard.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    pc_titles = PriceCard.objects.all()
    pc_descriptions = PriceCard.objects.all()
    price_table = PriceTable.objects.all()
    form = OrderForm()
    now = WhatYear()
    dict_obj = {'slider_list': slider_list,
                'products_card': products_card,
                'pc_titles': pc_titles,
                'pc_descriptions': pc_descriptions,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'price_table': price_table,
                'form': form,
                'now': now,
                }
    return render(request, './index.html', dict_obj)


# def thanks_page(request):        # Отправка данных при помощи метода GET
#     name = request.GET['name']
#     phone = request.GET['phone']
#     element = Order(order_name=name, order_phone=phone)
#     element.save()
#     return render(request, './thanks_page.html', {'name': name,
#                                                   'phone': phone})

def thanks_page(request):        # Отправка данных при помощи метода POST
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        sendTelegram(tg_name = name, tg_phone = phone)
        return render(request, './thanks_page.html', {'name': name,})
    else:
        return render(request, './thanks_page.html')

