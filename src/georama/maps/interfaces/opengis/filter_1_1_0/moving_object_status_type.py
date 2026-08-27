from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_slice_type import (
    AbstractTimeSliceType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.direction_property_type import (
    DirectionPropertyType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.location import Location
from georama.maps.interfaces.opengis.filter_1_1_0.measure_type import MeasureType
from georama.maps.interfaces.opengis.filter_1_1_0.priority_location import (
    PriorityLocation,
)
from georama.maps.interfaces.opengis.filter_1_1_0.status import Status

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MovingObjectStatusType(AbstractTimeSliceType):
    """This type encapsulates various dynamic properties of moving objects (points,
    lines, regions).

    It is useful for dealing with features whose geometry or topology
    changes over time.
    """

    priority_location_or_location: PriorityLocation | Location | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "priorityLocation",
                    "type": PriorityLocation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "location",
                    "type": Location,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    speed: MeasureType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bearing: DirectionPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    acceleration: MeasureType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    elevation: MeasureType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    status: Status | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
