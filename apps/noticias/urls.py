
from django.urls import path

from . import views

app_name = 'noticias'
# la url comienza con /Noticias/.. (ver apps\noticias\views.py)
urlpatterns = [
    
    path('listar/', views.listar, name = 'listar_noticias'),
    # URL PARA VISTA BASADA EN FUNCION
    #path('detalle/<int:pk>', views.Detalle_Noticia_Funcion, name = 'detalle_noticias'),
    # URL PARA VISTA BASADA EN CLASE
    path('detalle/<int:pk>', views.Detalle_Noticia_Clase.as_view(), name = 'detalle_noticias'),
    path("add_comentario/<int:pk>", views.Agregar_Comentario, name="agregar_comentario")

]
