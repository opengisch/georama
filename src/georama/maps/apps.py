from qgis_server_light.interface.dispatcher.redis_asio import RedisQueue

from georama.core.apps import GeoramaAbstractConfig
from georama.maps.maps_config import Config

central_app_label = "maps"

qsl_redis_queue = RedisQueue.create(Config().redis_url)


class MapsConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Maps"
    name = f"georama.{central_app_label}"
    label = central_app_label
    menu_order: int = 40
