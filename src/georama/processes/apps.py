from qgis_server_light.interface.dispatcher.redis_asio import RedisQueue
from qgis_server_light.interface.exporter.extract import Process
from qgis_server_light.interface.job.process.process_list import available
from xsdata.formats.dataclass.parsers import DictDecoder

from georama.core.apps import GeoramaAbstractConfig
from georama.maps.maps_config import Config

central_app_label = "processes"

qsl_redis_queue = RedisQueue.create(Config().redis_url)
qsl_available_processes = DictDecoder().decode(available, Process)


class ProcessConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Processes"
    name = f"georama.{central_app_label}"
    label = central_app_label
    menu_order: int = 60
