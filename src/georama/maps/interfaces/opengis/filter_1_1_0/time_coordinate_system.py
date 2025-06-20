from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.time_coordinate_system_type import (
    TimeCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCoordinateSystem(TimeCoordinateSystemType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
