from enum import Enum
from typing import List

from xsdata.formats.dataclass.serializers import XmlSerializer

from georama.maps.models import PublishedAsWms
from georama.maps.services import OgcOperation
from maps.interfaces.ogc.wms_1_3_0.exceptions.service_exceptions_1_3_0 import ServiceExceptionReport, ServiceException


class WmsExceptionCode(str, Enum):
    INVALID_FORMAT = ("InvalidFormat", "Request contains a FORMAT not offered by the server.")
    INVALID_CRS = ("InvalidCRS", "Request contains a CRS not offered by the server for one or more layers.")
    LAYER_NOT_DEFINED = ("LayerNotDefined", "Requested LAYER not offered by the server.")
    STYLE_NOT_DEFINED = ("StyleNotDefined", "Requested STYLE not offered by the server.")
    LAYER_NOT_QUERYABLE = ("LayerNotQueryable", "GetFeatureInfo requested on a layer not marked as queryable.")
    INVALID_POINT = ("InvalidPoint", "GetFeatureInfo request contains invalid I/J values.")
    CURRENT_UPDATE_SEQUENCE = ("CurrentUpdateSequence", "UPDATESEQUENCE parameter matches current version; no update required.")
    INVALID_UPDATE_SEQUENCE = ("InvalidUpdateSequence", "UPDATESEQUENCE parameter higher than current version.")
    MISSING_DIMENSION_VALUE = ("MissingDimensionValue", "Required dimension value is missing and no default provided.")
    INVALID_DIMENSION_VALUE = ("InvalidDimensionValue", "Provided dimension value is invalid.")
    OPERATION_NOT_SUPPORTED = ("OperationNotSupported", "Requested operation not supported by the server.")

    def __new__(cls, code: str, message: str):
        obj = str.__new__(cls, code)
        obj._value_ = code
        obj.message = message
        return obj



class WmsError(Exception):
    def __init__(self, exception_code: WmsExceptionCode, additional_msg: str = ""):
        self.code = str(exception_code.value)  # e.g. "LayerNotDefined"
        self.message = (
            f"{exception_code.message} {additional_msg}".strip()
        )  # removes trailing space if no extra msg
        super().__init__(self.message)

    def __str__(self) -> str:
        """Provides a user-friendly string representation."""
        return f"WMS Error ({self.code}): {self.message}"



class WmsOperation(OgcOperation):
    def obtain_accessible_layers(
        self, layer_names: List[str] | None = None
    ) -> List[PublishedAsWms]:
        accessible_layers = []
        if layer_names:
            query = self.model.objects.filter(name__in=layer_names)
        else:
            query = self.model.objects.filter()
        found_layers = query.all()
        if layer_names:
            found_difference = set(layer_names) - {layer.name for layer in found_layers}
            if len(found_difference) > 0:
                raise WmsError(WmsExceptionCode.LAYER_NOT_DEFINED, f"Layer(s) not found: {list(found_difference)}")
        for published_as in found_layers:
            if published_as.has_read_permission(self.user, self.appname):
                accessible_layers.append(published_as)
        if layer_names:
            permission_difference = set(layer_names) - {
                layer.name for layer in accessible_layers
            }
            if len(permission_difference) > 0:
                raise WmsError(WmsExceptionCode.LAYER_NOT_DEFINED, f"Layer(s) not permitted: {list(permission_difference)}")
        return accessible_layers

    @staticmethod
    def create_operation_parsing_failed(exception_message: str, exception_code: str = None) -> ServiceExceptionReport:
        """
        Generic method to create a valid error response XML.
        """
        return ServiceExceptionReport(service_exception=[ServiceException(value=exception_message, code=exception_code)])

    def render_operation_parsing_failed(self, exception_message: str, exception_code: str=None) -> str:

        serializer = XmlSerializer()

        return serializer.render(
            self.create_operation_parsing_failed(
                exception_message=exception_message,
                exception_code=exception_code,
            ),
            ns_map={
                None: "http://www.opengis.net/ogc",
                "xlink": "http://www.w3.org/1999/xlink",
            },
        )
