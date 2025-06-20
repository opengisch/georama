from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.label_style_property_type import (
    LabelStylePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LabelStyle2(LabelStylePropertyType):
    class Meta:
        name = "labelStyle"
        namespace = "http://www.opengis.net/gml"
