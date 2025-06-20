from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.vertical_crsref_type import (
    VerticalCrsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCrsref(VerticalCrsrefType):
    class Meta:
        name = "verticalCRSRef"
        namespace = "http://www.opengis.net/gml"
