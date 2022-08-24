from django.shortcuts import render
from .models import Evento
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin # para clases
# Create your views here.

class ListaEvento(LoginRequiredMixin, ListView):
    model = Evento
    context_object_name = "eventos"
    template_name = 'eventos/listar_eventos.html'
    

class DetalleEvento(LoginRequiredMixin, DetailView):
    model = Evento
    context_object_name = "evento"
    template_name = 'eventos/detalle_evento.html'