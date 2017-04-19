# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from . models import People
# Create your views here.
def index(request):
    People.objects.create(first_name="Theodore", last_name="The Third")
    people = People.objects.all()
    print people
    return render(request, 'third_app/index.html')