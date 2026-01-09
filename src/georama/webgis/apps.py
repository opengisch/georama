from georama.core.apps import GeoramaAbstractConfig
from django.utils.translation import gettext_lazy as _


class WebgisConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = _("WebGIS")
    name = "georama.webgis"
