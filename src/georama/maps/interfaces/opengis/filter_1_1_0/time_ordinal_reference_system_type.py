from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_reference_system_type import (
    AbstractTimeReferenceSystemType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.time_ordinal_era_type import (
    TimeOrdinalEraPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalReferenceSystemType(AbstractTimeReferenceSystemType):
    """
    In an ordinal reference system the order of events in time can be well
    established, but the magnitude of the intervals between them can not be
    accurately determined (e.g. a stratigraphic sequence).
    """

    component: list[TimeOrdinalEraPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
