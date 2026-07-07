from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_operation_ref_type import (
    CoordinateOperationRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationRef(CoordinateOperationRefType):
    class Meta:
        name = "coordinateOperationRef"
        namespace = "http://www.opengis.net/gml"
