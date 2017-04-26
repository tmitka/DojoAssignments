from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^employee_process$', views.employees_process),
    url(r'^employees$', views.employee),
    url(r'^assign_employee/(?P<id>\d+)$', views.assign_employee, name='employee'),
    url(r'^user/(?P<id>\d+)$', views.user, name='user'),
    url(r'^delete_employee/(?P<employee_id>\d+)/from/(?P<manager_id>\d+)$', views.delete, name='delete')
]