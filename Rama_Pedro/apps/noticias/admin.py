from django.contrib import admin

# Register your models here.

from .models import Noticia, Categoria
# en el sitio 'admin' registrar 'Noticia' y 'Categoria'
admin.site.register(Noticia)
admin.site.register(Categoria)



