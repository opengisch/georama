from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.pass_through_operation_ref_type import (
    PassThroughOperationRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PassThroughOperationRef(PassThroughOperationRefType):
    class Meta:
        name = "passThroughOperationRef"
        namespace = "http://www.opengis.net/gml"
