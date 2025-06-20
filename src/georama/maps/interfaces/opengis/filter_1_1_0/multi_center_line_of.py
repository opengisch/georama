from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_curve_property_type import (
    MultiCurvePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCenterLineOf(MultiCurvePropertyType):
    class Meta:
        name = "multiCenterLineOf"
        namespace = "http://www.opengis.net/gml"
