from georama.core.apps import GeoramaAbstractConfig
from django.utils.translation import gettext_lazy as _


class QfieldLinkConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "georama.qfield_link"
    verbose_name = _("QField Link")
