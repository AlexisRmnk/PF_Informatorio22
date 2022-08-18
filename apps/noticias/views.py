from django.shortcuts import render
from .models import Noticia


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required # para funciones
from django.contrib.auth.mixins import LoginRequiredMixin # para clases

# Create your views here.

def listar(request):
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

# VISTA BASADA EN FUNCIONES
@login_required #descorador, se ejecutan antes de las funciones
def Detalle_Noticia_Funcion(request, pk): #de ejemplo, no se usa
	ctx = {}
	noticia = Noticia.objects.get(pk = pk)
	ctx['resultado'] = noticia
	return render(request,'noticias/detalle_noticia.html',ctx)

#VISTA BASADA EN CLASES
class Detalle_Noticia_Clase(LoginRequiredMixin, DetailView):
	model = Noticia
	template_name = 'noticias/detalle_noticia.html'
    
#SI USO UNA VISTA BASADA EN CLASE EL CONTEXTO SE LLAMA:
# SI ES UNO SOLO object
# SI SON MUCHOS SE LLAMA object_list