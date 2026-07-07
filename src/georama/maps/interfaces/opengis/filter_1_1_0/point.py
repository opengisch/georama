from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.point_type import PointType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Point(PointType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
