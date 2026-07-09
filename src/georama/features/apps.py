import pygeoapi.api as inittime_api
import pygeoapi.plugin
from django.utils.translation import gettext_lazy as _

from georama.core.common.apps import GeoramaAbstractConfig
from georama.features.features_config import Config


class FeaturesConfig(GeoramaAbstractConfig):
    label = "features"
    name = "georama.features"
    menu_order: int = 10
    description = _("Share feature layers.")
    app_index_page = "features:featurelayer-list"


pygeoapi.plugin.PLUGINS["provider"]["OG_OGR"] = (
    "georama.features.pygeoapi_providers.ogr.GeoramaOgcProvider"
)

pygeoapi.plugin.PLUGINS["provider"]["OG_SQL"] = (
    "georama.features.pygeoapi_providers.sql.GeoramaSqlProvider"
)

inittime_api.DEFAULT_CRS = Config().default_crs
