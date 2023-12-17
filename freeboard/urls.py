from django.urls import path
from django.conf.urls import include
from freeboard import views

urlpatterns = [
    path('', views.index, name='freeboard-list'),
    path('<int:pk>/', views.single_post_page, name='free-post'),
    path('write/', views.write, name='free-write')
]