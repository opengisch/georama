from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.operation_method_ref_type import (
    OperationMethodRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationMethodRef(OperationMethodRefType):
    class Meta:
        name = "operationMethodRef"
        namespace = "http://www.opengis.net/gml"
