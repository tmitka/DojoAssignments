# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.messages import get_messages
from django.contrib import messages
import re
from models import User, Author, Book, Review
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

def index(request):
    return render(request, 'book_app/index.html')

def register_process(request):
    
    if request.method == "POST":

        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['email']
        password = request.POST['password']


        failed_validation = False

        if len(name) < 2:
            messages.error(request, "Name must be at least 2 characters")
            failed_validation = True

        if len(alias) < 2:
            messages.error(request, "Alias must be at least 2 characters")
            failed_validation = True

        try:
            user_exists = User.objects.get(email=email)
        except:
            user_exists = False

        if len(email) < 1:
            messages.error(request, "Email is required")
            failed_validation = True

        elif not EMAIL_REGEX.match(email):
            messages.error(request, "Please enter a valid email!")
            failed_validation = True

        elif user_exists:
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

        User.objects.create(name=name, alias=alias, email=email, password=password)

        request.session['current_user'] = User.objects.get(email=email).id

        return redirect('/books')
    
def books(request):
    if "current_user" in request.session.keys():
    
        context = {
            "user":User.objects.get(pk=request.session['current_user']),
            'messages':get_messages(request),
            'authors':Author.objects.all(),
            'books':Book.objects.all(),
            'reviews':Review.objects.all().order_by('-created_at')[:3]
        }

        return render(request, 'book_app/books.html', context)

    return render(request, 'book_app/books.html')

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
            return redirect('/books')

def add_book(request):
    if "current_user" in request.session.keys():
        
        context = {
            "user":User.objects.get(pk=request.session['current_user']),
            'messages':get_messages(request),
            'authors':Author.objects.all()
        }
        print books
    return render(request, 'book_app/add.html', context)

def add_process(request):
    
    if request.method == 'POST':

        review_validation = True

        title = request.POST['book_title']
        print title

        if len(title) < 1:
            review_validation = False
            messages.error(request, 'Title needed')
        
        author = ''
        if request.POST['author'] != '':
            author = request.POST['author']
            print author
        
        else:
            author = request.POST['new_author']
            print author

            if author:
                try:
                    author_exists = Author.objects.get(name=author)
                    author = author_exists.id
                except:
                    Author.objects.create(name=author)
                    author = Author.objects.get(name=author).id

        if not author:
            review_validaton = False
            messages.error(request, "Author cannot be left blank")


        review = request.POST['review']
        print review
        if len(review) < 1:
            review_validation = False
            messages.error(request, "Review cannot be left blank")
            print review

        rating = request.POST['rating']
        print rating
        
        if review_validation:
            Book.objects.create(title=title, author=Author.objects.get(pk=int(author)))
            user_review = User.objects.get(pk=request.session['current_user'])
            book = Book.objects.get(title='book_title')
            Review.objects.create(review=review, rating=rating, book=book, user_review=user_review)
            book_id = Book.objects.get(title=title).id
            


        return redirect('/books/' + str(book_id))
    
def new_book(request, id):
    if "current_user" in request.session.keys():
        book = Book.objects.get(pk=id)
        review_id = book.id
        context = {
            "user":User.objects.get(pk=request.session['current_user']),
            'book': book,
            'reviews':Review.objects.filter(book_id=id).order_by('-created_at')[:3]
        }
    return render(request, 'book_app/new.html', context)

def review_process(request, id):
    
    if request.method == 'POST':

        review_validation = True

        review = request.POST['review']
        print review
        if len(review) < 1:
            review_validation = False
            messages.error(request, "Review cannot be left blank")
            print review

        rating = request.POST['rating']
        print rating
        if review_validation:
            user_review = User.objects.get(pk=request.session['current_user'])
            book = Book.objects.get(pk=id)
            Review.objects.create(review=review, rating=rating,  book=book, user_review=user_review)

        return redirect('/books/' + str(id))
        
def user_process(request, id):
    return redirect('/users/' + str(id))

def users(request, id):
    if "current_user" in request.session.keys():
        book = Book.objects.get(pk=id)
        context = {
            "user":User.objects.get(pk=request.session['current_user']),
            'book': book,
            'reviews':Review.objects.filter(book_id=id).order_by('-created_at')[:3]
        }
    return render(request, 'book_app/users.html', context)
    pass