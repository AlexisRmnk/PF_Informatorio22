
from django.db import models

# Create your models here.

# class Calendario(models.Model):
#     pass

class Evento(models.Model):
    titulo =  models.CharField(max_length = 120)
    descripcion = models.TextField()
    fecha = models.DateField()
    es_gratuito = models.BooleanField()
    es_presencial = models.BooleanField()
    ubicacion =  models.CharField(max_length = 120)
    imagen = models.ImageField(verbose_name="Imagen opcion",
                               upload_to = 'eventos', null = True, blank = True)