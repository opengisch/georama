from georama.core.apps import GeoramaAbstractConfig
from django.utils.translation import gettext_lazy as _


class DataintegrationConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "georama.data_integration"
    verbose_name = _("Data Integration")
