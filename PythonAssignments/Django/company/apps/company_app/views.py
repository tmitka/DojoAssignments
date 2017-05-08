# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from models import Employee, Team
def index(request):
    return render(request, 'company_app/index.html')

def employees_process(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Employee.objects.create(first_name=first_name, last_name=last_name)
        return redirect('/employees')
    return redirect('/')

def employee(request):
    context = {
        'employees':Employee.objects.all()
    }
    return render(request, 'company_app/employees.html', context)

def assign_employee(request, id):
    Team.objects.create(manager_id=id, member_id=request.POST['employee_id'])
    return redirect(reverse('user', kwargs={'id':id}))

def user(request, id):
    employee = Employee.objects.get(id=id)
    context = {
        'current_employee': employee,
        'employees':Employee.objects.exclude(id=id),
        'manager_employees':Team.objects.filter(manager_id=id)
    }
    return render(request, 'company_app/managers.html', context)

def delete(request, employee_id, manager_id):
    employee_to_delete = Team.objects.filter(member_id=employee_id, manager_id=manager_id)
    employee_to_delete.delete()
    return redirect(reverse('user', kwargs={'id':manager_id}))