
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('register/',views.register),
    path('login/', views.login, name='login'),          
    path('lotteria/', views.lotteria, name='lotteria'),
]
