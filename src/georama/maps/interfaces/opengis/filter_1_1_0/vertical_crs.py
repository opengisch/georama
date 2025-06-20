from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.vertical_crstype import (
    VerticalCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCrs(VerticalCrstype):
    class Meta:
        name = "VerticalCRS"
        namespace = "http://www.opengis.net/gml"
