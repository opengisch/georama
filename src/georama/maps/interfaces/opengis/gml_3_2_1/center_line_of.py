from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.curve_property_type import (
    CurvePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CenterLineOf(CurvePropertyType):
    class Meta:
        name = "centerLineOf"
        namespace = "http://www.opengis.net/gml/3.2"
