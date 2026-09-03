from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.aggregation_type import (
    AggregationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_property_type import (
    SurfaceMember,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ShellType:
    surface_member: list[SurfaceMember] = field(
        default_factory=list,
        metadata={
            "name": "surfaceMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    aggregation_type: AggregationType | None = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
