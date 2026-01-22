from georama.core.apps import GeoramaAbstractConfig


class QfieldLinkConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "QFieldLink"
    name = "georama.qfield_link"
    label = "qfield_link"

    def ready(self):
        # TODO: remove this, once ready. We dont want to register a menu for Core on the Page
        pass
