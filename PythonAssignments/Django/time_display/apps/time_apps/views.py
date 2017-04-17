# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import datetime

def index(request):
    time = datetime.datetime.now()
    return render(request, 'time_apps/index.html')
