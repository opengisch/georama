from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.location_property_type import (
    LocationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Location(LocationPropertyType):
    """
    Deprecated in GML 3.1.0.
    """

    class Meta:
        name = "location"
        namespace = "http://www.opengis.net/gml"
