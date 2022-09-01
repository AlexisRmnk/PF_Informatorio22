from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2awi$098mo1txo-f%)ns!3@7h++aph&u1tc8vjm=237=y)z6i3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# Esto es para conectar a la BBDD de sqlite. Es mas ligero y simple. 
# NO SE INSTALA. Solo se usa en entornos de PRUEBA
# Es mas facil de compartir por GIT paraque todos los miembros de un grupo
# trabajan sobre lo mismo. 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9o32ljn8ro7j4',
        'USER': 'ijuvicfrdnejfe',
        'PASSWORD': '83928143467a1c158928bc8619812122fcd8ccf57878f0a40d3e8073c3e281cd',
        'HOST': 'ec2-34-227-135-211.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATICFILES_DIRS = (BASE_DIR, 'static')