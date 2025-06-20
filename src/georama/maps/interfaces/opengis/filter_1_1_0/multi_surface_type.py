from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.surface_members import SurfaceMembers
from georama.maps.interfaces.opengis.filter_1_1_0.surface_property_type import (
    SurfaceMember,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceType(AbstractGeometricAggregateType):
    """
    A MultiSurface is defined by one or more Surfaces, referenced through
    surfaceMember elements.
    """

    surface_member: list[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface_members: Optional[SurfaceMembers] = field(
        default=None,
        metadata={
            "name": "surfaceMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
