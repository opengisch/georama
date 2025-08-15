from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.moving_object_status import (
    MovingObjectStatus,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class HistoryPropertyType:
    """
    The history relationship associates a feature with a sequence of TimeSlice
    instances.
    """

    moving_object_status: list[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
