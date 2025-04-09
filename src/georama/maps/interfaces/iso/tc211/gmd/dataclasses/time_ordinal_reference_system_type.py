from dataclasses import dataclass, field
from typing import List

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_ordinal_era_type import (
    TimeOrdinalEraPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_reference_system_type import (
    TimeReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalReferenceSystemType(TimeReferenceSystemType):
    component: List[TimeOrdinalEraPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
