from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.engineering_crstype import (
    EngineeringCrstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringCrs(EngineeringCrstype):
    class Meta:
        name = "EngineeringCRS"
        namespace = "http://www.opengis.net/gml"
