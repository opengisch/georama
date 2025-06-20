from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.cylindrical_cstype import (
    CylindricalCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CylindricalCs(CylindricalCstype):
    class Meta:
        name = "CylindricalCS"
        namespace = "http://www.opengis.net/gml"
