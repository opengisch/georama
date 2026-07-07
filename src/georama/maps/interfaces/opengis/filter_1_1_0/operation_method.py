from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.operation_method_type import (
    OperationMethodType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationMethod(OperationMethodType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
