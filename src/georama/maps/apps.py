from georama.core.apps import GeoramaAbstractConfig

central_app_label = "maps"


class MapsConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Maps"
    name = f"georama.{central_app_label}"
    label = central_app_label
    menu_order: int = 30
