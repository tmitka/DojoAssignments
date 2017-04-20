# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Products

def index(request):
    Products.objects.create(name='Dark Souls 3', description='action rpg for xbox one', weight='2lbs', price='$40', cost='$50', category='game')
    products = Products.objects.all()
    for p in products:
        print p.name, p.description, p.weight, p.price, p.cost, p.category
    return render(request, 'product_app/index.html')