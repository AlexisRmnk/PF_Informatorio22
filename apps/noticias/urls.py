
from django.urls import path

from . import views

app_name = 'noticias'
# la url comienza con /Noticias/.. (ver apps\noticias\views.py)
urlpatterns = [
    
    path('listar/', views.Listar, name = 'listar_noticias'),
]
