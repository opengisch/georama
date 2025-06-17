from georama.core.apps import GeoramaAbstractConfig


class DataintegrationConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "georama.data_integration"
    verbose_name = "Data Integration"
