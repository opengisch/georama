from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinate_system_axis_property_type import (
    CoordinateSystemAxisPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemAxisRef(CoordinateSystemAxisPropertyType):
    class Meta:
        name = "coordinateSystemAxisRef"
        namespace = "http://www.opengis.net/gml"
