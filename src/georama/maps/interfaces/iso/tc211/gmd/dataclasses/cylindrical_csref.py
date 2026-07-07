from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cylindrical_csproperty_type import (
    CylindricalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CylindricalCsref(CylindricalCspropertyType):
    class Meta:
        name = "cylindricalCSRef"
        namespace = "http://www.opengis.net/gml"
