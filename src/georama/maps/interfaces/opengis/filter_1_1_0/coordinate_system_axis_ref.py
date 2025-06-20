from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_system_axis_ref_type import (
    CoordinateSystemAxisRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemAxisRef(CoordinateSystemAxisRefType):
    class Meta:
        name = "coordinateSystemAxisRef"
        namespace = "http://www.opengis.net/gml"
