from django.urls import path
from django.conf.urls import include
from requestboard import views

urlpatterns = [
    path('', views.index, name='requestboard-list'),
    path('<int:pk>/', views.single_post_page, name='request-post'),
    path('write/', views.write, name='request-write')
]