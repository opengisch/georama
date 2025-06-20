from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.rectangle_type import RectangleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Rectangle(RectangleType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
