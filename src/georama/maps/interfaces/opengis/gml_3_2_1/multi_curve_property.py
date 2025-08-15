from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.multi_curve_property_type import (
    MultiCurvePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurveProperty(MultiCurvePropertyType):
    class Meta:
        name = "multiCurveProperty"
        namespace = "http://www.opengis.net/gml/3.2"
