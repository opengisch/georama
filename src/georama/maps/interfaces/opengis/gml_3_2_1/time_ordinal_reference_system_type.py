from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.time_ordinal_era_type import (
    TimeOrdinalEraPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.time_reference_system_type import (
    TimeReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeOrdinalReferenceSystemType(TimeReferenceSystemType):
    component: list[TimeOrdinalEraPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
