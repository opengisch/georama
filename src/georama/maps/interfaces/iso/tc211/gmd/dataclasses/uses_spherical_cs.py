from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.spherical_csproperty_type import (
    SphericalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesSphericalCs(SphericalCspropertyType):
    class Meta:
        name = "usesSphericalCS"
        namespace = "http://www.opengis.net/gml"
