from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.cartesian_csref_type import (
    CartesianCsrefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CartesianCsref(CartesianCsrefType):
    class Meta:
        name = "cartesianCSRef"
        namespace = "http://www.opengis.net/gml"
