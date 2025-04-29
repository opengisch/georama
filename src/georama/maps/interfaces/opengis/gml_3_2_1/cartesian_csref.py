from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.cartesian_csproperty_type import (
    CartesianCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class CartesianCsref(CartesianCspropertyType):
    class Meta:
        name = "cartesianCSRef"
        namespace = "http://www.opengis.net/gml/3.2"
