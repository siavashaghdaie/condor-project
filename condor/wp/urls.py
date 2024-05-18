from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('company/', views.company, name = 'company'),
    path('contact/', views.contact, name = 'contact'),
    path('know-how/', views.knowHow, name = 'know-how'),
    path('new/', views.news, name = 'news'),
    path('solutions', views.solutions, name = 'solutions'),
]
