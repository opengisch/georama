from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.point_member import PointMember
from georama.maps.interfaces.opengis.gml_3_2_1.point_members import PointMembers

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiPointType(AbstractGeometricAggregateType):
    point_member: list[PointMember] = field(
        default_factory=list,
        metadata={
            "name": "pointMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_members: PointMembers | None = field(
        default=None,
        metadata={
            "name": "pointMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
