from georama.core.apps import GeoramaAbstractConfig


class WebgisConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Webgis"
    name = "georama.webgis"
    label = "webgis"

    def ready(self):
        # TODO: remove this, once ready. We dont want to register a menu for Core on the Page
        pass
