from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.geodesic_string_type import (
    GeodesicStringType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeodesicString(GeodesicStringType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
