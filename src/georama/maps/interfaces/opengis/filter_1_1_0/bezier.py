from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.bezier_type import BezierType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Bezier(BezierType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
