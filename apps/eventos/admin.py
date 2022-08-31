from django.contrib import admin
from .models import Evento, Categoria

# Register your models here.

admin.site.register(Evento)
admin.site.register(Categoria)