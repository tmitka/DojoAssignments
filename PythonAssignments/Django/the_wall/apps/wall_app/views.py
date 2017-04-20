# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Users, Messages, Comments

def index(request):
    return render(request, 'wall_app/index.html')