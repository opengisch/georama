from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.vertical_csref_type import (
    VerticalCsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCsref(VerticalCsrefType):
    class Meta:
        name = "verticalCSRef"
        namespace = "http://www.opengis.net/gml"
