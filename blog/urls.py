#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^about/$', views.about),
    url(r'^post/$', views.post),
    url(r'^contact/$', views.contact),
    url(r'^write_blog/$', views.write_blog),
    url(r'^get_blog/$', views.get_blog),
]
