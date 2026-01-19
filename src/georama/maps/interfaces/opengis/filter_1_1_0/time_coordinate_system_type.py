from dataclasses import dataclass, field
from typing import Optional, Union

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

    origin_position_or_origin: Optional[Union[TimePositionType, TimeInstantPropertyType]] = (
        field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "originPosition",
                        "type": TimePositionType,
                        "namespace": "http://www.opengis.net/gml",
                    },
                    {
                        "name": "origin",
                        "type": TimeInstantPropertyType,
                        "namespace": "http://www.opengis.net/gml",
                    },
                ),
            },
        )
    )
    interval: Optional[TimeIntervalLengthType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
