from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.cylindrical_csref_type import (
    CylindricalCsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CylindricalCsref(CylindricalCsrefType):
    class Meta:
        name = "cylindricalCSRef"
        namespace = "http://www.opengis.net/gml"
