
from django.db import models

# Create your models here.

# class Calendario(models.Model):
#     pass

class Categoria(models.Model):
    titulo =  models.CharField(max_length = 60)
    descripcion = models.TextField()
    def __str__(self) -> str:
        return self.titulo
    def get_eventos_categoria(self):
        return self.evento_set.all()

class Evento(models.Model):
    titulo =  models.CharField(max_length = 120)
    descripcion = models.TextField()
    fecha = models.DateField()
    es_gratuito = models.BooleanField()
    es_presencial = models.BooleanField()
    ubicacion =  models.CharField(max_length = 120)
    imagen = models.ImageField(verbose_name="Imagen opcional",
                               upload_to = 'eventos', null = True, blank = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    
    def __str__(self) -> str:
        return self.titulo