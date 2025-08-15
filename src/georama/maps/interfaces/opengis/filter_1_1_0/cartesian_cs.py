from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.cartesian_cstype import (
    CartesianCstype,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CartesianCs(CartesianCstype):
    class Meta:
        name = "CartesianCS"
        namespace = "http://www.opengis.net/gml"
