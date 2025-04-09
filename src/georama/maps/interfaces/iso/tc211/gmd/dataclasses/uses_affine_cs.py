from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.affine_csproperty_type import (
    AffineCspropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesAffineCs(AffineCspropertyType):
    class Meta:
        name = "usesAffineCS"
        namespace = "http://www.opengis.net/gml"
