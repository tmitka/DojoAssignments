from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^email_process$', views.email_process),
    url(r'^emails$', views.emails),
    url(r'emails/(?P<email_id>\d+)/delete$', views.delete)
]