from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.single_operation_ref_type import (
    SingleOperationRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SingleOperationRef(SingleOperationRefType):
    class Meta:
        name = "singleOperationRef"
        namespace = "http://www.opengis.net/gml"
