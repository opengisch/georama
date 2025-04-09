from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ellipsoid_type import (
    EllipsoidType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Ellipsoid1(EllipsoidType):
    """A gml:Ellipsoid is a geometric figure that may be used to describe the
    approximate shape of the earth.

    In mathematical terms, it is a surface formed by the rotation of an
    ellipse about its minor axis.
    """

    class Meta:
        name = "Ellipsoid"
        namespace = "http://www.opengis.net/gml"
