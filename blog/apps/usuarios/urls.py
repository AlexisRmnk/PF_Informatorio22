from django.urls import path 

from . import views

urlpatterns = [
    
    path('login/', views.Login, name = 'log__in'),
]
