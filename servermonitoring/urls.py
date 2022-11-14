from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('secure/', views.secure),
    path('server/<id>', views.get_server_info),
]