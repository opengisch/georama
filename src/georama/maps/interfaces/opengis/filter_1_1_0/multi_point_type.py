from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.point_member import PointMember
from georama.maps.interfaces.opengis.filter_1_1_0.point_members import PointMembers

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPointType(AbstractGeometricAggregateType):
    """
    A MultiPoint is defined by one or more Points, referenced through pointMember
    elements.
    """

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
