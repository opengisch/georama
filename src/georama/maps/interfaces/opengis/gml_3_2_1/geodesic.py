from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.geodesic_type import GeodesicType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Geodesic(GeodesicType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
