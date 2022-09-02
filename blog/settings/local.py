from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2awi$098mo1txo-f%)ns!3@7h++aph&u1tc8vjm=237=y)z6i3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# Esto es para conectar a la BBDD de sqlite. Es mas ligero y simple. 
# NO SE INSTALA. Solo se usa en entornos de PRUEBA
# Es mas facil de compartir por GIT paraque todos los miembros de un grupo
# trabajan sobre lo mismo. 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# https://sqlitebrowser.org/
# para trabajar con sql lite


# esto es para conectar a la BBDD de sql server
# es mas 'poderoso' y seguro
'''
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME':'TPFINAL',
        'Trusted_Connection':'yes',
        'HOST': 'localhost',
        'OPTIONS':{
        	'driver':'SQL Server Native Client 11.0',
        }
    },
}

'''