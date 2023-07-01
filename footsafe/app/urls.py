from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.category, name='category'),
    path('contribute/', views.contribute, name='contribue'),
    path('contactus/', views.contactus, name='contactus'),
]