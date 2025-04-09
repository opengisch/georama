from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.curve_members import CurveMembers
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.curve_property_type import (
    CurveMember,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCurveType(AbstractGeometricAggregateType):
    curve_member: List[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve_members: Optional[CurveMembers] = field(
        default=None,
        metadata={
            "name": "curveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
