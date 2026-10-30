from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from georama.core.common.apps import GeoramaAbstractConfig


class WebGisConfig(GeoramaAbstractConfig):
    label = "webgis"
    name = "georama.webgis"
    menu_order: int = 10
    description = _("Publish your Layers in a WebGIS.")
    app_index_page = "webgis:theme-list"

    def ready(self):
        from georama.core.common.remote_actions import RemoteAction, register_remote_action
        from georama.integration.models import Project

        super().ready()
        rma = RemoteAction(
            target=reverse("webgis:theme-manager-publish-from-project"),
            name=_("Theme"),
            icon_classes="fa fa-circle-plus",
            help_text=_("Publishes this Project as a Theme in the WebGis app."),
            origin=self.name,
            permissions=["webgis.add_theme"],
        )
        register_remote_action(Project, rma)
