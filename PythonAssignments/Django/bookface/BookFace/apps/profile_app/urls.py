from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.login),
    url(r'^login_process$', views.login_process),
    url(r'^register$', views.register),
    url(r'^register_process$', views.register_process)
]