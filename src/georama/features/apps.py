import pygeoapi.api as inittime_api
import pygeoapi.plugin
from django.apps import AppConfig

from georama.features.features_config import Config

# add custom providers to pygeoapi
print("loading provider")

pygeoapi.plugin.PLUGINS["provider"][
    "OG_POSTGRES"
] = "georama.features.pygeoapi_providers.postgres.PostgresProvider"


inittime_api.DEFAULT_CRS = Config().default_crs

appname = "features"


class VectorparrotConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = f"georama.{appname}"
