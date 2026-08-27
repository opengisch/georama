from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_members import (
    SurfaceMembers,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_property_type import (
    SurfaceMember,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceType(AbstractGeometricAggregateType):
    surface_member: list[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface_members: SurfaceMembers | None = field(
        default=None,
        metadata={
            "name": "surfaceMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
