from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_curve_type import MultiCurveType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCurve(MultiCurveType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
