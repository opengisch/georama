from django.apps import AppConfig

appname = 'rasteroctopus'


class RasteroctopusConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = f'georama.{appname}'
