from django.shortcuts import render
from .models import Noticia

# Create your views here.

def Listar(request):
    # creo diccionario CONTEXT para pasar datos al template
    ctx = dict()
    # BUSCAR LAS NOTICIAS EN LA BD
    
    # BUSCAR LO QUE QUIERTO EN LA BD
    todas_noticias = Noticia.objects.all() # devuelve un diccionario de objeto
    # de tipo Noticia
    # print(todas_noticias) # esto se imprime en la consola del CMD cuando 
    # iniciamos el servidor con 'python manage.py runserver' y luego vamos a
    # la vista de noticias
    
    # PASARLO AL TEMPLATE
    ctx['notis'] = todas_noticias
    
    return render(request, 'noticias/listar_noticias.html', ctx) 
    # todo lo de return se envia al template (templates\noticias\listar_noticias.html)
    # el template no recibe el diccionario completo. Recibe variables.
    # Cada variable es la clave del diccionario.
    # El template tendra una variable NOTIS.
    
# EJEMPLO DE COMO EL TEMPLATE 'DESARMA' EL CTX
# ctx['nombre'] = 'Juan'
# ctx['notas'] = [7, 9, 6]

# EL TEMPLATE 
# nombre = 'Juan'
# notas = [7, 9, 6]