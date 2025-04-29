from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.spherical_cstype import SphericalCstype

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SphericalCs1(SphericalCstype):
    """Gml:SphericalCS is a three-dimensional coordinate system with one distance
    measured from the origin and two angular coordinates.

    A SphericalCS shall have three gml:axis property elements.
    """

    class Meta:
        name = "SphericalCS"
        namespace = "http://www.opengis.net/gml/3.2"
