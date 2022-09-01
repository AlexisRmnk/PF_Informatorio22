from django.db import models
from ..usuarios.models import Usuario
from datetime import date 


# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length = 60)
    descripcion = models.CharField(max_length = 250, null = True, blank = True)
    
    # relacion   >>>   CATEGORIA    1:N     NOTICIA
    # para acceder las noticias de una categoria, usar 
    # 'categoria.noticia_set.all' desde Django desde el template. Fuente: 
    # https://docs.djangoproject.com/en/3.2/intro/tutorial03/
    
    def __str__(self) -> str:
        return self.nombre
    def get_noticias_categoria(self):
        return self.noticia_set.all()

 
class Noticia(models.Model):
    titulo = models.CharField(max_length = 120)
    creado = models.DateField(auto_now_add = True)
    cuerpo = models.TextField()
    autor = models.CharField(max_length = 50, null = True, blank = True, 
                             default="Botellas de Amor")
    imagen = models.ImageField(upload_to = 'noticias', null = True, blank = True)
    # 'null' es para que la BD acepte valores nulos. 'Blank' es para que el 
    # formulario (la entrada) permita valores VACIOS. Van los dos juntos.
    
    # la 'Noticia' va a tener un campo 'categoria' que va a ser una clave
    # foranea a la clase 'Categoria'. On_delete CASCADE  indica que si se borra
    # una categoria, automaticamente se van a borrar todas las notis de esa cat.
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE, 
                                  null = True)
    # noticia.comentario_set.all
    
    def __str__(self) -> str:
        return self.titulo
    def get_comentarios_noticia(self):
        return self.comentario_noticia.all() #similar a noticia.comentario_set.all
    
# relacion   >>>   NOTICIA    1:N     COMENTARIOS
# OPCIONAL: relacion   >>>   USUARIO    1:N     COMENTARIOS
class Comentario(models.Model):
    contenido_txt = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    noticia = models.ForeignKey(Noticia, on_delete = models.CASCADE, 
                                null = False, related_name="comentario_noticia")
    autor = models.ForeignKey(Usuario, on_delete = models.CASCADE, 
                                null = False, related_name="comentario_autor") 
    # imagen_adjunta = archivo tipo imagen
    
    
    