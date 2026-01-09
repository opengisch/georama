from georama.core.apps import GeoramaAbstractConfig
from django.utils.translation import gettext_lazy as _


class MapsConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "georama.maps"
    verbose_name = _("Maps")
