from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_member import PointMember
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point_members import PointMembers

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPointType(AbstractGeometricAggregateType):
    point_member: list[PointMember] = field(
        default_factory=list,
        metadata={
            "name": "pointMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point_members: PointMembers | None = field(
        default=None,
        metadata={
            "name": "pointMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
