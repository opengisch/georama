from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.geodesic_type import GeodesicType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Geodesic(GeodesicType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
