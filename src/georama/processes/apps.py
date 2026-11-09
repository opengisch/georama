from django.utils.translation import gettext_lazy as _
from qgis_server_light.dispatcher.redis_asio import RedisQueue, RedisStateQueue

from georama.core.apps import GeoramaAbstractConfig
from georama.maps.maps_config import Config

central_app_label = "processes"

qsl_redis_queue = RedisQueue.create(Config().redis_url)
qsl_redis_state_queue = RedisStateQueue.create(Config().redis_url)


class ProcessConfig(GeoramaAbstractConfig):
    label = "processes"
    name = "georama.processes"
    menu_order: int = 10
    description = _("OGC API Processes.")
    app_index_page = "processes:api-landing"
