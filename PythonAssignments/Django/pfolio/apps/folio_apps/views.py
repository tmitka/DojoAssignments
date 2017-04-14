# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    return render(request, 'folio_apps/index.html')

def testimonials(request):
    return render(request, 'folio_apps/testimonials.html')