import logging
from pathlib import Path

from django.conf import settings
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

    def ready(self):
        super().ready()
        global_folder_name = settings.DATA_INTEGRATION_GLOBAL_ORGANISATION_FOLDER
        global_folder_path = Path(settings.DATA_INTEGRATION_ROOT / global_folder_name)
        if not global_folder_path.exists():
            logging.info("Global organisation data integration folder created")
            global_folder_path.mkdir()
        elif not global_folder_path.is_dir():
            raise Exception(f"A file already exists at {global_folder_name}")
        else:
            logging.debug(f"Global organisation folder {global_folder_name} already created")
