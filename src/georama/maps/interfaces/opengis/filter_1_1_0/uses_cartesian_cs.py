from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.cartesian_csref_type import (
    CartesianCsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesCartesianCs(CartesianCsrefType):
    """
    Association to the Cartesian coordinate system used by this CRS.
    """

    class Meta:
        name = "usesCartesianCS"
        namespace = "http://www.opengis.net/gml"
