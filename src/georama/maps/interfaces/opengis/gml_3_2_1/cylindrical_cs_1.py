from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.cylindrical_cstype import (
    CylindricalCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CylindricalCs1(CylindricalCstype):
    """Gml:CylindricalCS is a three-dimensional coordinate system consisting of a
    polar coordinate system extended by a straight coordinate axis perpendicular to
    the plane spanned by the polar coordinate system.

    A CylindricalCS shall have three gml:axis property elements.
    """

    class Meta:
        name = "CylindricalCS"
        namespace = "http://www.opengis.net/gml/3.2"
