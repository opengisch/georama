from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.triangle_type import TriangleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Triangle(TriangleType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
