# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=250)
    weight = models.CharField(max_length=10)
    price = models.CharField(max_length=10) 
    cost= models.CharField(max_length=10)
    category = models.CharField(max_length=50)
