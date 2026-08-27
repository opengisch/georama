from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.curve_members import CurveMembers
from georama.maps.interfaces.opengis.gml_3_2_1.curve_property_type import CurveMember

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MultiCurveType(AbstractGeometricAggregateType):
    curve_member: list[CurveMember] = field(
        default_factory=list,
        metadata={
            "name": "curveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    curve_members: CurveMembers | None = field(
        default=None,
        metadata={
            "name": "curveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
