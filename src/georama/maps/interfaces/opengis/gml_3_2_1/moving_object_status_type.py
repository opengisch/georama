from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_slice_type import (
    AbstractTimeSliceType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.direction_property_type import (
    DirectionPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.geometry_array_property_type import (
    GeometryPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.location import Location
from georama.maps.interfaces.opengis.gml_3_2_1.location_name import LocationName
from georama.maps.interfaces.opengis.gml_3_2_1.location_reference import (
    LocationReference,
)
from georama.maps.interfaces.opengis.gml_3_2_1.measure_type import MeasureType
from georama.maps.interfaces.opengis.gml_3_2_1.pos import Pos
from georama.maps.interfaces.opengis.gml_3_2_1.priority_location import PriorityLocation
from georama.maps.interfaces.opengis.gml_3_2_1.status import Status
from georama.maps.interfaces.opengis.gml_3_2_1.status_reference import StatusReference

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MovingObjectStatusType(AbstractTimeSliceType):
    position: Optional[GeometryPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pos: Optional[Pos] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    location_name: Optional[LocationName] = field(
        default=None,
        metadata={
            "name": "locationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    location_reference: Optional[LocationReference] = field(
        default=None,
        metadata={
            "name": "locationReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    priority_location: Optional[PriorityLocation] = field(
        default=None,
        metadata={
            "name": "priorityLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    speed: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    bearing: Optional[DirectionPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    acceleration: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    elevation: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    status: Optional[Status] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    status_reference: Optional[StatusReference] = field(
        default=None,
        metadata={
            "name": "statusReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
