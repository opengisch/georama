from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.spherical_csproperty_type import (
    SphericalCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphericalCs2(SphericalCspropertyType):
    """
    Gml:sphericalCS is an association role to the spherical coordinate system used
    by this CRS.
    """

    class Meta:
        name = "sphericalCS"
        namespace = "http://www.opengis.net/gml"
