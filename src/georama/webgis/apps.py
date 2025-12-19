from georama.core.apps import GeoramaAbstractConfig


class WebgisConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Web GIS"
    name = "georama.webgis"
