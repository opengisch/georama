from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinate_system_property_type import (
    CoordinateSystemPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesCs(CoordinateSystemPropertyType):
    class Meta:
        name = "usesCS"
        namespace = "http://www.opengis.net/gml"
