from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.affine_csproperty_type import (
    AffineCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesAffineCs(AffineCspropertyType):
    class Meta:
        name = "usesAffineCS"
        namespace = "http://www.opengis.net/gml/3.2"
