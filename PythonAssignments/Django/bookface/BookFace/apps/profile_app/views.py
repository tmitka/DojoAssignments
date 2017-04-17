# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import User
from django.contrib import messages
def login(request):
    return render(request, 'profile_app/login.html')

def login_process(request):
    if request.method == "POST":
        server_email = request.POST['html_email']
        server_password = request.POST["html_password"]

        try:
            user = User.objects.get(email=server_email)
            if user.password == server_password:
                request.session['user_id']= user.id
            else:
                messages.error(request, "Passwords do not match")
                return redirect('/profile/login')
        except:
            messages.error(request, "User does not exist, please register")
            return redirect('/profile/register')



    return redirect('/profile/login')

def register(request):
    return render(request, 'profile_app/register.html')

def register_process(request):
    if request.method == "POST":
        server_email = request.POST['html_email']
        server_password =request.POST['html_password']
        confirm_password = request.POST['html_confirm']

        if confirm_password == server_password:
            try:
                user = User.objects.create(email=server_email, password=server_password)
                request.session['user_id']= user.id
                
            except:
                messages.error(request, "This user already exists")

    return redirect('/profile/register')


