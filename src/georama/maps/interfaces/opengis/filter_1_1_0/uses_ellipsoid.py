from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoid_ref_type import (
    EllipsoidRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesEllipsoid(EllipsoidRefType):
    """
    Association to the ellipsoid used by this geodetic datum.
    """

    class Meta:
        name = "usesEllipsoid"
        namespace = "http://www.opengis.net/gml"
