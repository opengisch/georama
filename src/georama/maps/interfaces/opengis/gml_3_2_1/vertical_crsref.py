from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.vertical_crsproperty_type import (
    VerticalCrspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalCrsref(VerticalCrspropertyType):
    class Meta:
        name = "verticalCRSRef"
        namespace = "http://www.opengis.net/gml/3.2"
