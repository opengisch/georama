from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.association_role_type import (
    AssociationRoleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class RangeParameters(AssociationRoleType):
    class Meta:
        name = "rangeParameters"
        namespace = "http://www.opengis.net/gml/3.2"
