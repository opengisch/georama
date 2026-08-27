from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_primitive_type import (
    TimeInstantPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.time_interval_length_type import (
    TimeIntervalLengthType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.time_position_type import (
    TimePositionType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.time_reference_system_type import (
    TimeReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeCoordinateSystemType(TimeReferenceSystemType):
    origin_position: TimePositionType | None = field(
        default=None,
        metadata={
            "name": "originPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    origin: TimeInstantPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    interval: TimeIntervalLengthType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
