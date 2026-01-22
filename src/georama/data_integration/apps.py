from django.utils.translation import gettext_lazy as _

from georama.core.apps import GeoramaAbstractConfig

central_app_label = "data_integration"


class DataintegrationConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    label = central_app_label
    name = f"georama.{central_app_label}"
    verbose_name = _("Data Integration")
