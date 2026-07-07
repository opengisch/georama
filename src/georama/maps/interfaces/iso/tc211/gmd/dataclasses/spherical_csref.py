from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.spherical_csproperty_type import (
    SphericalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphericalCsref(SphericalCspropertyType):
    class Meta:
        name = "sphericalCSRef"
        namespace = "http://www.opengis.net/gml"
