# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'portfolio_apps/index.html')

def testimonials(request):
    return render(request, 'portfolio_apps/testimonials.html')