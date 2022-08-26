from django.shortcuts import render

def Home(request):
	return render(request,'index.html')

def Login(request):
    return render(request, 'usuarios/log_in.html')

def Register(request):
    return render(request, 'usuarios/sign_up.html')

def Contact(request):
    return render(request, 'contactos/Contact-form.html')

def Noticias(request):
    return render(request, 'noticias/noticias.html')

def SobreNosotros(request):
    return render(request, 'sobre nosotros/about_us.html')

def Calendario(request):
    return render(request, 'eventos/calendario.html')