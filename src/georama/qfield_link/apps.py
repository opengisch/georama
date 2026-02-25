import logging

from django.conf import settings

from georama.core.apps import GeoramaAbstractConfig

central_app_label = "qfield_link"


class QfieldLinkConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "QFieldLink"
    name = f"georama.{central_app_label}"
    label = central_app_label
    menu_order: int = 15

    def app_permissions(self):
        return [f"{self.label}.can_use_app"]

    def ready(self):
        if (
            settings.QFIELD_LINK_URL
            and settings.QFIELD_LINK_USER
            and settings.QFIELD_LINK_PASSWORD
        ):
            super().ready()
        else:
            logging.info(
                "Omitting QFIELD Cloud linking tool since configuration is not complete."
            )
