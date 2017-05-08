from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_process$', views.register_process),
    url(r'^books$', views.books),
    url(r'^logout$', views.logout),
    url(r'^login_process$', views.login_process),
    url(r'^books/add', views.add_book),
    url(r'^add_process$', views.add_process),
    url(r'^books/(?P<id>\d+)$', views.new_book),
    url(r'^review_process/(?P<id>\d+)$', views.review_process, name ="add_review"),
    url(r'^user_process/(?P<id>\d+)$', views. user_process, name = 'user'),
    url(r'^users/(?P<id>\d+)$', views.users),
    url(r'^books/(?P<id>\d+)$', views.books, name="book")
]
