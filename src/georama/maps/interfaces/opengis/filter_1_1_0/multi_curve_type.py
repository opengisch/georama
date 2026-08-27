from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.curve_members import CurveMembers
from georama.maps.interfaces.opengis.filter_1_1_0.curve_property_type import CurveMember

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiCurveType(AbstractGeometricAggregateType):
    """
    A MultiCurve is defined by one or more Curves, referenced through curveMember
    elements.
    """

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
