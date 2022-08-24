from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.usuarios'
    # siempre agregar el 'apps.' en la linea de arriba para indicar donde esta
    # la aplicacion (en la carpeta APPS en este caso).

