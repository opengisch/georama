from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.spherical_cstype import (
    SphericalCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SphericalCs1(SphericalCstype):
    """Gml:SphericalCS is a three-dimensional coordinate system with one distance
    measured from the origin and two angular coordinates.

    A SphericalCS shall have three gml:axis property elements.
    """

    class Meta:
        name = "SphericalCS"
        namespace = "http://www.opengis.net/gml"
