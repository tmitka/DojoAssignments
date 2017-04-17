# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.crypto import get_random_string
from django.shortcuts import render, redirect

def index(request):
    if 'count' in request.session.keys():
        request.session['count'] += 1
        request.session['random_word'] = get_random_string(length=14)
    else:
        request.session['count'] = 0

    if request.session['count'] == 0:
            request.session['random_word'] = ""
        

    return render(request, 'random_apps/index.html')

def reset(request):
  request.session['count'] = -1
  return redirect('/')