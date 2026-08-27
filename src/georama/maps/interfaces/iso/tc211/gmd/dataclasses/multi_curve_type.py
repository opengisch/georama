from dataclasses import dataclass, field

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
    curve_member: list[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve_members: CurveMembers | None = field(
        default=None,
        metadata={
            "name": "curveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
