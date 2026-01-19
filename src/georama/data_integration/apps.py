from django.utils.translation import gettext_lazy as _

from georama.core.apps import GeoramaAbstractConfig
from georama.core.menu import MenuItem, register_menu_item


class DataintegrationConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "georama.data_integration"
    verbose_name = _("Data Integration")

    @classmethod
    def app_menu(cls):
        return MenuItem(
            label=cls.verbose_name,
            url_name="georama.data_integration:index",
            order=10,
        )

    def ready(self):
        register_menu_item(self.app_menu())
