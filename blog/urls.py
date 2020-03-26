from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', post_detail, name = "post_detail"),
    url(r'post_create/$', post_create, name='post_create'),
]