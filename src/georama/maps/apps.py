from django.utils.translation import gettext_lazy as _
from qgis_server_light.interface.dispatcher.redis_asio import RedisQueue

from georama.core.common.apps import GeoramaAbstractConfig
from georama.maps.maps_config import Config

central_app_label = "maps"

qsl_redis_queue = RedisQueue.create(Config().redis_url)


class MapsConfig(GeoramaAbstractConfig):
    label = "maps"
    name = "georama.maps"
    menu_order: int = 10
    description = _("Share map layers.")
    app_index_page = "maps:maplayer-list"
