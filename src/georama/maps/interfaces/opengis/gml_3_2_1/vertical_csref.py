from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.vertical_csproperty_type import (
    VerticalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalCsref(VerticalCspropertyType):
    class Meta:
        name = "verticalCSRef"
        namespace = "http://www.opengis.net/gml/3.2"
