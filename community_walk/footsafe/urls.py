from django.contrib import admin
from django.urls import path
from footsafe import views

urlpatterns = [     
    path('', views.home_view,name='home'),
]