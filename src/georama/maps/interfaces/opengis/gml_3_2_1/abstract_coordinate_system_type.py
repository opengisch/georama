from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType
from georama.maps.interfaces.opengis.gml_3_2_1.axis import Axis
from georama.maps.interfaces.opengis.gml_3_2_1.identified_object_type import (
    IdentifiedObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.uses_axis import UsesAxis

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCoordinateSystemType(IdentifiedObjectType):
    uses_axis: list[UsesAxis] = field(
        default_factory=list,
        metadata={
            "name": "usesAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    axis: list[Axis] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
