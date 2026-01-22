from georama.core.apps import GeoramaAbstractConfig


class MapsConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Maps"
    name = "georama.maps"
    label = "maps"

    def ready(self):
        # TODO: remove this, once ready. We dont want to register a menu for Core on the Page
        pass
