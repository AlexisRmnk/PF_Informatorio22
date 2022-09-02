from django.shortcuts import render
from .models import Noticia, Categoria, Comentario
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.core.paginator import Paginator
#from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required # para funciones
from django.contrib.auth.mixins import LoginRequiredMixin # para clases

# Create your views here.

def listar(request):
    # creo diccionario CONTEXT para pasar datos al template
    ctx = dict()
    # BUSCAR LAS NOTICIAS EN LA BD
    
    # BUSCAR LO QUE QUIERO EN LA BD
    #  todas_noticias = Noticia.objects.all() # devuelve un diccionario 
    # de objeto de tipo Noticia
    # print(todas_noticias) # esto se imprime en la consola del CMD cuando 
    # iniciamos el servidor con 'python manage.py runserver' y luego vamos a
    # la vista de noticias
    
    # orden_noticias = request.POST.get('orden_noticias_name')
    # mas_antiguas // mas_recientes
    
    if request.method == "POST":
        categoria_id = request.POST.get('categoria_name', 'todas')
        orden_noticias = request.POST.get('orden_noticias_name','mas_recientes')
        if categoria_id == "todas":
            noticias = Noticia.objects.all()
        else:
            cate = Categoria.objects.get(pk = categoria_id)
            print(f"Nombre categoria es: {cate.nombre}")
            noticias = cate.get_noticias_categoria()
        for n in noticias:
            print(n)
        
        if orden_noticias == 'mas_recientes':
            noticias = noticias.order_by("-creado")
        else:
            noticias = noticias.order_by("creado")
    else: 
        noticias = Noticia.objects.order_by('-creado') #las mas nuevas primero
    
    todas_noticias_paginadas = Paginator(noticias, 4) # por defecto 8
    pagina_solicitada = request.GET.get('page')
    noticias_paginadas_solicitada = todas_noticias_paginadas.get_page(pagina_solicitada)
    
    # PASARLO AL TEMPLATE
    ctx['noticias'] = noticias_paginadas_solicitada
    
    todas_categorias = Categoria.objects.all()
    ctx["categorias"] = todas_categorias
    
    
    
    return render(request, 'noticias/news.html', ctx) 
    # todo lo de return se envia al template (templates\noticias\listar_noticias.html)
    # el template no recibe el diccionario completo. Recibe variables.
    # Cada variable es la clave del diccionario.
    # El template tendra una variable NOTICIAS.
    
# EJEMPLO DE COMO EL TEMPLATE 'DESARMA' EL CTX
# ctx['nombre'] = 'Juan'
# ctx['notas'] = [7, 9, 6]

# EL TEMPLATE 
# nombre = 'Juan'
# notas = [7, 9, 6]


# VISTA BASADA EN FUNCIONES
#@login_required #descorador, se ejecutan antes de las funciones
def Detalle_Noticia_Funcion(request, pk): #de ejemplo, no se usa
	ctx = {}
	noticia = Noticia.objects.get(pk = pk)
	ctx['resultado'] = noticia
	return render(request,'noticias/Mientras/ModalNoticias.html',ctx)

#VISTA BASADA EN CLASES
#class Detalle_Noticia_Clase(LoginRequiredMixin, DetailView):
class Detalle_Noticia_Clase(DetailView):
    model = Noticia
    template_name = 'noticias/Mientras/ModalNoticias.html'
    context_object_name = "noticia"
 
    
#SI USO UNA VISTA BASADA EN CLASE EL CONTEXTO SE LLAMA:
# SI ES UNO SOLO object
# SI SON MUCHOS SE LLAMA object_list


def Agregar_Comentario(request, pk):
    texto_comentario = request.POST.get('coment')
    # 2 formas de crear un comentario
    # forma 1:
    noti = Noticia.objects.get(pk = pk)
    Comentario.objects.create(noticia = noti, contenido_txt = texto_comentario, autor = request.user)
    # forma 2
    # c = Comentario()
    # c.noticia = pk
    # c.texto = texto_comentario
    # c.autor = request.user
    # c.save()
    
    return HttpResponseRedirect(reverse_lazy("noticias:detalle_noticias", kwargs={"pk":pk}))
