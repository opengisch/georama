from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinate_operation_property_type import (
    CoordinateOperationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationRef(CoordinateOperationPropertyType):
    class Meta:
        name = "coordinateOperationRef"
        namespace = "http://www.opengis.net/gml"
