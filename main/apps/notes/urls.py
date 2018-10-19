from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^snippet.html$', views.all_html),
    url(r'^create$', views.create)
]
