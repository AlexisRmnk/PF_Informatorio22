"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# esto permite que el servidor acceda a la carpeta MEDIA (Imports)
from django.conf.urls.static import static
from django.conf import settings

# para URL LOGIN
from django.contrib.auth import views as auth_views

from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', 
         auth_views.LoginView.as_view(template_name="usuarios/log_in.html"),
         name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('sobrenosotros/', views.SobreNosotros, name = 'sobrenosotros'),
    path('preguntasFQ/', views.PreguntasFQ, name = 'preguntasFQ'),
    path('noticia_detalles/', views.NoticiaDetalles, name = 'noticia_detalles'),
    
    
    path('', views.Home, name = 'home'),
    # URL DE APLICACIONES
    path('Noticias/', include('apps.noticias.urls')),
    path('Eventos/', include('apps.eventos.urls')),
    path('Usuario/',include('apps.usuarios.urls')),
    path('Contactos/', include('apps.contactos.urls')), # no olvidar coma al final
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    # esto permite que el servidor acceda a la carpeta MEDIA