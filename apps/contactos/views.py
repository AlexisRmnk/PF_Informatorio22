from django.shortcuts import render
#from models import Formulario

# Create your views here.

def info_contacto(request):
    return render(request, 'contactos/info_contactos.html')

# pendiente: ver como hacer el INPUT del que se contacte
def contactanos(request):
    return render(request, 'contactos/contactanos.html')

def enviar_contacto(request):
    # WIP
    pass