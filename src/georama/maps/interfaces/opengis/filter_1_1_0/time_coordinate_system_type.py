from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_primitive_type import (
    TimeInstantPropertyType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_reference_system_type import (
    AbstractTimeReferenceSystemType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.time_interval_length_type import (
    TimeIntervalLengthType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.time_position_type import (
    TimePositionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeCoordinateSystemType(AbstractTimeReferenceSystemType):
    """
    A temporal coordinate system is based on a continuous interval scale defined in
    terms of a single time interval.
    """

    origin_position: Optional[TimePositionType] = field(
        default=None,
        metadata={
            "name": "originPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    origin: Optional[TimeInstantPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    interval: Optional[TimeIntervalLengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
