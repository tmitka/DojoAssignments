# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updatedd_at = models.DateTimeField(auto_now=True)

class Team(models.Model):
    manager = models.ForeignKey(Employee, related_name='employee_manager')
    member = models.ForeignKey(Employee, related_name='employee_member')
    created_at = models.DateTimeField(auto_now_add=True)
    updatedd_at = models.DateTimeField(auto_now=True)

