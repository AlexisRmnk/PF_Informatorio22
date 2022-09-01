from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('listar/', views.listar, name = 'listar_eventos'),
    path('detalle/<int:pk>', views.DetalleEvento.as_view(), 
         name = 'detalle_eventos'),
    path('calendario/', views.Calendario, name = 'calendario'),
]
