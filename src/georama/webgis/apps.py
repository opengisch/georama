from georama.core.apps import GeoramaAbstractConfig

central_app_label = "webgis"


class WebgisConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Webgis"
    name = f"georama.{central_app_label}"
    label = central_app_label
    menu_order: int = 1
