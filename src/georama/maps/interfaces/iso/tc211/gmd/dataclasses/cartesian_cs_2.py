from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cartesian_csproperty_type import (
    CartesianCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CartesianCs2(CartesianCspropertyType):
    """
    Gml:cartesianCS is an association role to the Cartesian coordinate system used
    by this CRS.
    """

    class Meta:
        name = "cartesianCS"
        namespace = "http://www.opengis.net/gml"
