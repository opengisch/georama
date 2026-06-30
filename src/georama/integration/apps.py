from django.utils.translation import gettext_lazy as _

from georama.core.common.apps import GeoramaAbstractConfig


class IntegrationConfig(GeoramaAbstractConfig):
    label = "integration"
    name = "georama.integration"
    menu_order: int = 10
    description = _("Integrate your QGIS projects.")
    app_index_page = "integration:project-list"

    def app_permissions(self):
        return ["integration.view_collection"]
