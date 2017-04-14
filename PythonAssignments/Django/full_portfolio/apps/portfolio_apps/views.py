# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
def index(request):
    return render(request, 'portfolio_apps/index.html')

def projects(request):
    return render(request, 'portfolio_apps/projects.html')

def about(request):
    return render(request, 'portfolio_apps/about.html')

def testimonials(request):
    return render(request, 'portfolio_apps/testimonials.html')
