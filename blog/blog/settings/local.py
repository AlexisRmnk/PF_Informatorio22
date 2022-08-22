from .base import *


SECRET_KEY = 'django-insecure-cwd9bne^ytkj&r3fz4$zl3%v$tkoj#kejlo=0e+4s)x6yex=@@'


DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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