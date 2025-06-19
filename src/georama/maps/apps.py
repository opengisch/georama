from georama.core.apps import GeoramaAbstractConfig


class MapsConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Maps"
    name = "georama.maps"
