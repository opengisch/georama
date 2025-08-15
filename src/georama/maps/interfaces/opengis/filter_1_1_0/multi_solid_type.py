from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.composite_solid_type import (
    SolidMember,
)
from georama.maps.interfaces.opengis.filter_1_1_0.solid_members import SolidMembers

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolidType(AbstractGeometricAggregateType):
    """
    A MultiSolid is defined by one or more Solids, referenced through solidMember
    elements.
    """

    solid_member: list[SolidMember] = field(
        default_factory=list,
        metadata={
            "name": "solidMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid_members: Optional[SolidMembers] = field(
        default=None,
        metadata={
            "name": "solidMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
