from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.cartesian_csproperty_type import (
    CartesianCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CartesianCs2(CartesianCspropertyType):
    """
    Gml:cartesianCS is an association role to the Cartesian coordinate system used
    by this CRS.
    """

    class Meta:
        name = "cartesianCS"
        namespace = "http://www.opengis.net/gml/3.2"
