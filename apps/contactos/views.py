from django.shortcuts import render

from django.core.mail import send_mail

# Create your views here.

def info_contacto(request):
    return render(request, 'contactos/info_contactos.html')

# pendiente: ver como hacer el INPUT del que se contacte
def contactanos(request):
    return render(request, 'contactos/Contact-form.html')

# referencia: 
# https://martinfritz.medium.com/create-contact-form-and-send-emails-to-your-gmail-account-using-django-86ac6f739a86
# 
def enviar_contacto(request):
    nombre = request.POST['contacto_nombre_name']
    mensaje = request.POST['contacto_mensaje_name']
    email = request.POST['contacto_email_name']
    telefono = request.POST['contacto_telefono_name']
    
    form_data = {
        'nombre':nombre,
        'email':email,
        'telefono':telefono,
        'mensaje':mensaje,
        }
    mensaje = f'''
    Desde:\n\t\t{form_data['nombre']}\n
    Mensaje:\n\t\t{form_data['mensaje']}\n
    Email:\n\t\t{form_data['email']}\n
    Telefono:\n\t\t{form_data['telefono']}\n
    '''
    send_mail('Solicitud de contacto desde BOTELLAS_DE_AMOR', mensaje, '',
              ['testgrupo5pf@outlook.com.ar']) 
    return render(request, 'index.html')