# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'ninja_app/index.html')

def ninjas(request):
    return render(request, 'ninja_app/ninjas.html')

def ninja_color(request, color):
    context ={
        "ninja_color": color
    }
    return render(request, 'ninja_app/ninja_color.html', context)
