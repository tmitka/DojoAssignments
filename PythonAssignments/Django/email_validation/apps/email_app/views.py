# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import render, redirect
import re
from .models import Email

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    
    context = {
        'messages':get_messages(request)
    }

    return render(request, 'email_app/index.html', context)

def email_process(request):
    
    if request.method == "POST":
    
        email = request.POST['email']


        if len(email) < 1:
            messages.error(request, "Email cannot be blank")
        elif EMAIL_REGEX.match(email):

            print "Registering username"

            Email.objects.create(email=email)

            print Email.objects.all()


            messages.success(request, "You have registered this (" + email + ") address")
            return redirect('/emails')
        else:
            messages.error(request, "Please Enter a Valid Email Address!")
    return redirect('/')

def emails(request):
        
    context = {
        'messages': get_messages(request),
        'all_emails': Email.objects.all()
    }

    return render(request, 'email_app/emails.html', context)

def delete(request, email_id):
    
    Email.objects.get(pk=email_id).delete()

    return redirect('/emails')