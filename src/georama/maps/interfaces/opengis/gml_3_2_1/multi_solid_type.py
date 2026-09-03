from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.solid_members import SolidMembers
from georama.maps.interfaces.opengis.gml_3_2_1.solid_property_type import SolidMember

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiSolidType(AbstractGeometricAggregateType):
    solid_member: list[SolidMember] = field(
        default_factory=list,
        metadata={
            "name": "solidMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    solid_members: SolidMembers | None = field(
        default=None,
        metadata={
            "name": "solidMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
