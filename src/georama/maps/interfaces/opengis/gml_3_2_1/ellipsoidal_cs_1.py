from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.ellipsoidal_cstype import (
    EllipsoidalCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class EllipsoidalCs1(EllipsoidalCstype):
    """Gml:EllipsoidalCS is a two- or three-dimensional coordinate system in which
    position is specified by geodetic latitude, geodetic longitude, and (in the
    three-dimensional case) ellipsoidal height.

    An EllipsoidalCS shall have two or three gml:axis property elements;
    the number of associations shall equal the dimension of the CS.
    """

    class Meta:
        name = "EllipsoidalCS"
        namespace = "http://www.opengis.net/gml/3.2"
