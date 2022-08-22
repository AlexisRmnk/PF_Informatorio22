from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Noticia

def Listar(request):
	#Creo el diccionario para pasar datos al temaplte
	ctx = {}	
	#BUSCAR LO QUE QUIERO EN LA BD
	todas = Noticia.objects.all()
	#PASARLO AL TEMPLATE
	ctx['notis'] = todas

	return render(request,'noticias/listar_noticias.html',ctx)

# EJEMPLO DE COMO DESARMA EL CTX EL TEMPLATE.
# ctx['nombre'] = 'nicolas'
# ctx['notas'] = [5,6,9]
# EL TEMPLATE ya separa el diccionario
# nombre = 'nicolas'
# notas = [5,6,9]


#VISTA BASADA EN FUNCIONES
@login_required
def Detalle_Noticia_Funcion(request, pk):
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
# SI SON MUCHOS SE LLAMA obect_list
