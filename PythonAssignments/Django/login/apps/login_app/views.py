# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.messages import get_messages
from django.contrib import messages
import re
from models import User
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
def index(request):
    return render(request, 'login_app/index.html')


def register_process(request):

    if request.method == "POST":

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']


        failed_validation = False

        if len(first_name) < 2:
            messages.error(request, "First name must be at least 2 characters")
            failed_validation = True

        elif not NAME_REGEX.match(first_name):
            messages.error(request, "First name can only contain letters")
            failed_validation = True

        if len(last_name) < 2:
            messages.error(request, "Last name must be at least 2 characters")
            failed_validation = True

        elif not NAME_REGEX.match(last_name):
            messages.error(request, "Last name can only contain letters")
            failed_validation = True

        try:
            found_user = User.objects.get(email=email)
        except:
            found_user = False

        if len(email) < 1:
            messages.error(request, "Email is required")
            failed_validation = True

        elif not EMAIL_REGEX.match(email):
            messages.error(request, "Please enter a valid email!")
            failed_validation = True

        elif found_user:
            messages.error(request, "Email already exists")
            failed_validation = True

        if len(request.POST['password']) < 1:
            messages.error(request, "Password is required!")
            failed_validation = True

        elif len(request.POST['password']) < 8:
            messages.error(request, "Password must be at least 8 characters long.")
            failed_validation = True

        elif request.POST['confirm_password'] != request.POST['password']:
            messages.error(request, "Passwords must be the same")
            failed_validation = True

        if failed_validation:
            return redirect('/')

        User.objects.create(first_name=first_name, last_name=last_name, email=email, password=password)

        request.session['current_user'] = User.objects.get(email=email).id

        return redirect('/users')

def users(request):

    if "current_user" in request.session.keys():

        context = {
            "user":User.objects.get(pk=request.session['current_user']),
            'messages':get_messages(request)
        }
        
        return render(request, 'login_app/users.html', context)

    return render(request, 'login_app/users.html')

def logout(request):
    request.session.clear()
    messages.success(request, "Logged Out")

    return redirect('/')

def login_process(request):
    
    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        failed_authentication = False

        try:
            user_exists = User.objects.get(email=email)
        except:
            user_exists = False

        if len(email) < 1:
            messages.error(request, "Email cannot be left blank!")
            failed_authentication = True

        elif not EMAIL_REGEX.match(email):
            messages.error(request, "Please enter a valid email!")
            failed_authentication = True

        elif not user_exists:
            messages.error(request, "User does not exist. Please register.")
            failed_authentication = True

        if user_exists.password != password:
            messages.error(request, "Incorrect password! Please try again")
            failed_authentication = True


        if failed_authentication:
            return redirect('/')
        else:
            messages.success(request, 'Successfully logged in!')
            request.session['current_user'] = user_exists.id
            return redirect('/users')

