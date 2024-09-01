from django.apps import AppConfig

appname = 'vectorparrot'

class VectorparrotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = f'georama.{appname}'
