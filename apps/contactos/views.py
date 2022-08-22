from django.shortcuts import render
#from models import Formulario
from django.core.mail import send_mail, BadHeaderError

# Create your views here.

def info_contacto(request):
    return render(request, 'contactos/info_contactos.html')

# pendiente: ver como hacer el INPUT del que se contacte
def contactanos(request):
    return render(request, 'contactos/contactanos.html')

# referencia: 
# https://martinfritz.medium.com/create-contact-form-and-send-emails-to-your-gmail-account-using-django-86ac6f739a86
# 
def enviar_contacto(request):
    nombre = request.POST['contacto_nombre_name']
    mensaje = request.POST['contacto_mensaje_name']
    email = request.POST['contacto_email_name']
    telefono = request.POST['contacto_telefono_name']
    '''
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    message = request.POST.get('message')
    '''
    
    form_data = {
        'nombre':nombre,
        'email':email,
        'telefono':telefono,
        'mensaje':mensaje,
        }
    mensaje = '''
    From:\n\t\t{}\n
    Mensaje:\n\t\t{}\n
    Email:\n\t\t{}\n
    Telefono:\n\t\t{}\n
    '''.format(form_data['nombre'], form_data['mensaje'], form_data['email'],
               form_data['telefono'])
    send_mail('Solicitud de contacto desde BOTELLAS_DE_AMOR', mensaje, '',
              ['testgrupo5pf@outlook.com.ar']) # TODO: enter your email address
    return render(request, 'contactos/exito.html')