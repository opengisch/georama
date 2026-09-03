from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_time_primitive_type import (
    TimeInstantPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_interval_length_type import (
    TimeIntervalLengthType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_position_type import (
    TimePositionType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_reference_system_type import (
    TimeReferenceSystemType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCoordinateSystemType(TimeReferenceSystemType):
    origin_position: TimePositionType | None = field(
        default=None,
        metadata={
            "name": "originPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    origin: TimeInstantPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    interval: TimeIntervalLengthType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
