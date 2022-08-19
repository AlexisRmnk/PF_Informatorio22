from django.db import models

# es para contactarse con los dueños de la organizacion

class Formulario(models.Model):
    nombre = models.CharField(max_length=120)
    email = models.EmailField()
    mensaje = models.TextField(verbose_name="mensaje opcional", blank=True)
    fecha = models.DateField(auto_now_add=True) # preg profe 
    imagen = models.ImageField(verbose_name="imagen opcional",
                               upload_to = 'contactos', null = True, blank = True)
    
    def __str__(self) -> str:
        return self.mensaje