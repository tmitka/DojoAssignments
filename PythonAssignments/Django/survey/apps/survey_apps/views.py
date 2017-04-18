# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey_apps/index.html')

def form_process(request):
    if request.method == "POST":
        if 'count' in request.session.keys():
            request.session['count'] += 1
        else:
            request.session['count'] = 1
       
        name = request.POST['name']
        location = request.POST['location']
        language = request.POST['language']
        comment = request.POST['comment']
        request.session['name'] = name
        request.session['location'] = location
        request.session['language'] = language
        request.session['comment'] = comment
        return redirect('/results')
    else:
        return redirect('/')

def results(request):
    return render(request, 'survey_apps/results.html')
