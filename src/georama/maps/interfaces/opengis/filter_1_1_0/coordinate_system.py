from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_coordinate_system_type import (
    AbstractCoordinateSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateSystem(AbstractCoordinateSystemType):
    class Meta:
        name = "_CoordinateSystem"
        namespace = "http://www.opengis.net/gml"
