from django.shortcuts import render
from .models import Evento, Categoria
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin # para clases
from django.core.paginator import Paginator
from django.utils.safestring import mark_safe
from .utils import Calendar
from datetime import datetime, date, timedelta
import calendar
# Create your views here.

#UNUSED
#class ListaEvento(LoginRequiredMixin, ListView
class ListaEvento(ListView):
    model = Evento
    context_object_name = "eventos"
    template_name = 'eventos/listar_eventos.html'
    
def listar(request):
    ctx = dict()
    if request.method == "POST":
        categoria_id = request.POST.get('categoria_name', 'todos')
        orden_eventos = request.POST.get('orden_eventos_name','mas_proximos')
        if categoria_id == "todos":
            eventos = Evento.objects.all()
        else:
            cate = Categoria.objects.get(pk = categoria_id)
            print(f"Nombre categoria es: {cate.nombre}")
            eventos = cate.get_eventos_categoria()
        for n in eventos:
            print(n)
        
        if orden_eventos == 'mas_proximos':
            eventos = eventos.order_by("fecha")
        else:
            eventos = eventos.order_by("-fecha")
    else: 
        eventos = Evento.objects.order_by('fecha') #los mas proximos primero

    # por si se desean paginar (sin usar!)
    pag = Paginator(eventos, 1)
    page = request.GET.get('page')
    eventos_paginados = pag.get_page(page) 
    
    # PASARLO AL TEMPLATE
    ctx['eventos'] = eventos 
    todas_categorias = Categoria.objects.all()
    ctx["categorias"] = todas_categorias

    return render(request, 'eventos/listar_eventos.html', ctx) 
    
#class DetalleEvento(LoginRequiredMixin, DetailView):
class DetalleEvento(DetailView):
    model = Evento
    context_object_name = "evento"
    template_name = 'eventos/detalle_evento.html'
    
def Calendario(request): #del calendario sin back
    return render(request, 'eventos/calendario.html')

class CalendarView(ListView):
    model = Evento
    template_name = 'eventos/calendarioV2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        d = get_date(self.request.GET.get('month', None))
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

