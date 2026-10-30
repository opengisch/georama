import pygeoapi.api as inittime_api
import pygeoapi.plugin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from georama.core.common.apps import GeoramaAbstractConfig
from georama.features.features_config import Config


class FeaturesConfig(GeoramaAbstractConfig):
    label = "features"
    name = "georama.features"
    menu_order: int = 10
    description = _("Share feature layers.")
    app_index_page = "features:feature-list"

    def ready(self):
        from georama.core.common.remote_actions import RemoteAction, register_remote_action
        from georama.integration.models import Vector

        super().ready()
        rma = RemoteAction(
            target=reverse("features:feature-manager-publish-from-vector"),
            name=_("FeatureLayer"),
            icon_classes="fa fa-circle-plus",
            help_text=_(
                "Publishes this Vector Datasource as a new FeatureLayer in the Features app."
            ),
            origin=self.name,
            permissions=["features.add_featurelayer"],
        )
        register_remote_action(Vector, rma)


pygeoapi.plugin.PLUGINS["provider"]["OG_OGR"] = (
    "georama.features.pygeoapi_providers.ogr.GeoramaOgcProvider"
)

pygeoapi.plugin.PLUGINS["provider"]["OG_SQL"] = (
    "georama.features.pygeoapi_providers.sql.GeoramaSqlProvider"
)

inittime_api.DEFAULT_CRS = Config().default_crs
