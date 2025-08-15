from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.topo_curve_property_type import (
    TopoCurvePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoCurveProperty(TopoCurvePropertyType):
    class Meta:
        name = "topoCurveProperty"
        namespace = "http://www.opengis.net/gml"
