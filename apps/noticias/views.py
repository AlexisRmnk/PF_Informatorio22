from django.shortcuts import render
from .models import Noticia, Categoria, Comentario
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from django.core.paginator import Paginator
from django.views.generic.list import ListView
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
    # orden_noticias = request.POST.get('orden_noticias_name')
    # mas_antiguas // mas_recientes
    
<<<<<<< Updated upstream
    #paginación
    noticias1 = Noticia.objects.all()
    p = Paginator(noticias1, 2)
    page = request.GET.get('page')
    notis = p.get_page(page)
    
=======
    noticias1 = Noticia.objects.all()
    pag = Paginator(noticias1, 2)
    page = request.GET.get('page')
    notis = pag.get_page(page)
>>>>>>> Stashed changes
    
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

        #test:
        for n in notis:
            print(n.titulo, n.creado, type(n))
    
     
    
    # PASARLO AL TEMPLATE
    ctx['noticias'] = notis
    
    todas_categorias = Categoria.objects.all()
    ctx["categorias"] = todas_categorias
    
    return render(request, 'noticias/listar_noticias.html', ctx) 
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

def listar_inverso(request):
    
    noticias1 = Noticia.objects.order_by('creado')
    p = Paginator(noticias1, 2)
    page = request.GET.get('page')
    notis = p.get_page(page)
    
    ctx = dict()
    # noticias_orden_inverso = Noticia.objects.order_by('creado') #las mas  
                                                            # viejas primero
    for n in notis:
        print(n.titulo, n.creado, type(n))
    ctx['noticias'] = notis

    todas_categorias = Categoria.objects.all()
    ctx["categorias"] = todas_categorias
            
    return render(request, 'noticias/listar_noticias_inv.html', ctx)    


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
    context_object_name = "noticia"
 
    
#SI USO UNA VISTA BASADA EN CLASE EL CONTEXTO SE LLAMA:
# SI ES UNO SOLO object
# SI SON MUCHOS SE LLAMA object_list


def Agregar_Comentario(request, pk):
    texto_comentario = request.POST.get('comment')
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


    