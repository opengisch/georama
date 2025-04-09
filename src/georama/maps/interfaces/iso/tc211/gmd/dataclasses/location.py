from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.location_property_type import (
    LocationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Location(LocationPropertyType):
    class Meta:
        name = "location"
        namespace = "http://www.opengis.net/gml"
