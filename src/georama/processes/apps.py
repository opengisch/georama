from qgis_server_light.interface.dispatcher.redis_asio import RedisQueue
from qgis_server_light.interface.exporter import extract
from qgis_server_light.interface.job.process.process_list import available
from xsdata.formats.dataclass.parsers import DictDecoder
from xsdata.formats.dataclass.parsers.config import ParserConfig

from georama.core.apps import GeoramaAbstractConfig
from georama.maps.maps_config import Config

central_app_label = "processes"

qsl_redis_queue = RedisQueue.create(Config().redis_url)


def custom_class_factory(clazz, params):
    if issubclass(clazz, extract.ProcessingParameterType):
        # we see if the matched class is the right one and if not, we make it the right
        # one, this is necessary because we implemented ambiguous types in QSL interface
        match params["name"]:
            case "str":
                clazz = extract.ProcessingParameterTypeString
            case "bool":
                clazz = extract.ProcessingParameterTypeBoolean
            case "float":
                clazz = extract.ProcessingParameterTypeFloat
            case "int":
                clazz = extract.ProcessingParameterTypeInt
            case "extent":
                clazz = extract.ProcessingParameterTypeExtent
            case "crs":
                clazz = extract.ProcessingParameterTypeCrs
            case "band":
                clazz = extract.ProcessingParameterTypeBand
            case "field":
                clazz = extract.ProcessingParameterTypeField
            case "layout":
                clazz = extract.ProcessingParameterTypeLayout
            case "map_theme":
                clazz = extract.ProcessingParameterTypeMapTheme
            case "expression":
                clazz = extract.ProcessingParameterTypeExpression
            case "enum":
                clazz = extract.ProcessingParameterTypeEnum
            case "vector_layer":
                clazz = extract.ProcessingParameterTypeVectorLayer
            case "raster_layer":
                clazz = extract.ProcessingParameterTypeRasterLayer
            case "file":
                clazz = extract.ProcessingParameterTypeFile
            case "map_layer":
                clazz = extract.ProcessingParameterTypeMapLayer
            case "multiple_layers":
                clazz = extract.ProcessingParameterTypeAnyLayer

    return clazz(**params)


config = ParserConfig(class_factory=custom_class_factory)
qsl_available_processes = DictDecoder(config=config).decode(available, extract.Process)


class ProcessConfig(GeoramaAbstractConfig):
    default_auto_field = "django.db.models.BigAutoField"
    verbose_name = "Processes"
    name = f"georama.{central_app_label}"
    label = central_app_label
    menu_order: int = 60
