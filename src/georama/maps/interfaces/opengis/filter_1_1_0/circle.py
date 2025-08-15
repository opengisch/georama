from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.circle_type import CircleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Circle(CircleType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
