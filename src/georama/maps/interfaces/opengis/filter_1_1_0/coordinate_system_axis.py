from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_system_axis_type import (
    CoordinateSystemAxisType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystemAxis(CoordinateSystemAxisType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
