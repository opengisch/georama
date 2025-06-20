from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.polygon_type import PolygonType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Polygon(PolygonType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
