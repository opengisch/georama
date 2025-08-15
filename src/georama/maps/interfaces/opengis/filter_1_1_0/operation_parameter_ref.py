from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.operation_parameter_ref_type import (
    OperationParameterRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterRef(OperationParameterRefType):
    class Meta:
        name = "operationParameterRef"
        namespace = "http://www.opengis.net/gml"
