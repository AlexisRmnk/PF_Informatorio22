from django.urls import path, re_path
#from django.conf.urls import url
from . import views

app_name = 'eventos'

urlpatterns = [
    path('listar/', views.listar, name = 'listar_eventos'),
    path('detalle/<int:pk>', views.DetalleEvento.as_view(), 
         name = 'detalle_eventos'),
   # path('calendario/', views.Calendario, name = 'calendario'),
    path('calendario/', views.CalendarView.as_view(), name = 'calendario'),
    #url(r'^calendar/$', views.CalendarView.as_view(), name = 'calendario'),
]
