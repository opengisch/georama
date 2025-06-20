from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topo_curve_type import TopoCurveType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoCurve(TopoCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
