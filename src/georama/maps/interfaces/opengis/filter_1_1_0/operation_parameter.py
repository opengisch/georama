from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.operation_parameter_type import (
    OperationParameterType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameter(OperationParameterType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
