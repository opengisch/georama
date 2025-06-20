from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.history_property_type import (
    HistoryPropertyType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.moving_object_status import (
    MovingObjectStatus,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TrackType(HistoryPropertyType):
    """
    The track of a moving object is a sequence of specialized timeslices
    that indicate the status of the object.
    """

    moving_object_status: list[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
