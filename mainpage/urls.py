from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from mainpage import views

urlpatterns = [
    path('', views.index),

]
