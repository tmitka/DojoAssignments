# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Books
import datetime
def index(request):
    Books.objects.create(title='The Wise Mans fear', author='Patrick Rothfuss', category='fantasy')
    books = Books.objects.all()
    for b in books:
        print b.title, b.author, b.published_date, b.category
    return render(request, 'book_app/index.html')
