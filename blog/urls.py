from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^$', post_list, name='post_list'),
    url(r'^(?P<pk>\d+)/$', post_detail, name = "post_detail"),
    url(r'post_create/$', post_create, name='post_create'),
    url(r'^(?P<pk>\d+)/post_edit/$', post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/post_delete/$', post_delete, name='post_delete'),
    url(r'^(?P<pk>\d+)/favourite_post/$', favourite_post, name='favourite'),
    url(r'favourites/', post_favourite_list, name='post_favourite_list'),
]