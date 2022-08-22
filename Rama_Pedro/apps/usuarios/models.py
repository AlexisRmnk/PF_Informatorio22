# Aca vamos a poner los modelos que van a impactar en la BBDD


from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    # aca vamos a especificar las caracteristicas especificas del modelo de
    # user.
    pass
