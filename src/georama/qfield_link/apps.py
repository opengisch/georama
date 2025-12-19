from georama.core.apps import GeoramaAbstractConfig


class QfieldLinkConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "QField Link"
    name = "georama.qfield_link"
