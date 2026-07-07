from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.solid_members import SolidMembers
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.solid_property_type import (
    SolidMember,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolidType(AbstractGeometricAggregateType):
    solid_member: List[SolidMember] = field(
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
