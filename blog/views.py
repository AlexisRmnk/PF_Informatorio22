from django.shortcuts import render

def Home(request):
	return render(request,'index.html')

def Login(request):
    return render(request, 'log_in.html')

def Register(request):
    return render(request, 'usuarios/sign_up.html')

def Contact(request):
    return render(request, 'Contact-form.html')

def Noticias(request):
    return render(request, 'noticias.html')

def SobreNosotros(request):
    return render(request, 'about_us.html')