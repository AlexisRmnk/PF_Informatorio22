from django.shortcuts import render

def Home(request):
	return render(request,'index.html')

def Login(request):
    return render(request, 'usuarios/log_in.html')

def Register(request):
    return render(request, 'usuarios/sign_up.html')

def SobreNosotros(request):
    return render(request, 'sobre nosotros/sobre_nosotros.html')



def PreguntasFQ(request):
    return render(request, 'sobre nosotros/preguntas_frecuentes.html')

def NoticiaDetalles(request):
    return render(request, 'noticias/ModalNoticias.html')