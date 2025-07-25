import pygeoapi.api as inittime_api
import pygeoapi.plugin

from georama.core.apps import GeoramaAbstractConfig
from georama.features.features_config import Config

# add custom providers to pygeoapi
print("loading provider")

pygeoapi.plugin.PLUGINS["provider"][
    "OG_OGR"
] = "georama.features.pygeoapi_providers.ogr.GeoramaOgcProvider"

pygeoapi.plugin.PLUGINS["provider"][
    "OG_SQL"
] = "georama.features.pygeoapi_providers.sql.GeoramaSqlProvider"

inittime_api.DEFAULT_CRS = Config().default_crs


class FeaturesConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Features"
    name = "georama.features"
