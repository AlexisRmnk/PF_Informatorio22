from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2awi$098mo1txo-f%)ns!3@7h++aph&u1tc8vjm=237=y)z6i3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['informatorio2022.herokuapp.com']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# Esto es para conectar a la BBDD de sqlite. Es mas ligero y simple. 
# NO SE INSTALA. Solo se usa en entornos de PRUEBA
# Es mas facil de compartir por GIT paraque todos los miembros de un grupo
# trabajan sobre lo mismo. 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.pg2',
        'NAME': 'd73pvhhal9ggt6',
        'USER': 'okrydsichrcxwi',
        'PASSWORD': '2cb81e64853b6206ee455506ed737ed47deae06f591b786409d480604607b079',
        'HOST': 'ec2-35-168-122-84.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}