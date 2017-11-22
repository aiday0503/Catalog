from django.shortcuts import render
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^show/(?P<id>\d+)$', views.show),
    url(r'^removeitem/(?P<id>\d+)$', views.removeitem),
    url(r'^additem/(?P<id>\d+)$', views.additem),
    url(r'^createitem/(?P<id>\d+)$', views.createitem),   
    url(r'^logout$', views.logout),
]
   
    
    