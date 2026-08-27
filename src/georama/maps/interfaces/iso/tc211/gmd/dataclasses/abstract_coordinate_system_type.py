from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.aggregation_type import (
    AggregationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.axis import Axis
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.identified_object_type import (
    IdentifiedObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.uses_axis import UsesAxis

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractCoordinateSystemType(IdentifiedObjectType):
    uses_axis: list[UsesAxis] = field(
        default_factory=list,
        metadata={
            "name": "usesAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    axis: list[Axis] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    aggregation_type: AggregationType | None = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
