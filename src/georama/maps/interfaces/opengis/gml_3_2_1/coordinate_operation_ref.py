from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_operation_property_type import (
    CoordinateOperationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CoordinateOperationRef(CoordinateOperationPropertyType):
    class Meta:
        name = "coordinateOperationRef"
        namespace = "http://www.opengis.net/gml/3.2"
