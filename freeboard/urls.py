from django.urls import path
from django.conf.urls import include
from freeboard import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.single_post_page)
]