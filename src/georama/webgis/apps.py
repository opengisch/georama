from georama.core.apps import GeoramaAbstractConfig


class WebgisConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Webgis"
    name = f"georama.webgis"
