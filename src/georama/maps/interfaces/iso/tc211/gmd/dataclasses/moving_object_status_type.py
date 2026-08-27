from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_time_slice_type import (
    AbstractTimeSliceType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.direction_property_type import (
    DirectionPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.geometry_array_property_type import (
    GeometryPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.location import Location
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.location_name import LocationName
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.location_reference import (
    LocationReference,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.measure_type import MeasureType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pos import Pos
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.priority_location import (
    PriorityLocation,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.status import Status
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.status_reference import (
    StatusReference,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MovingObjectStatusType(AbstractTimeSliceType):
    position: GeometryPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pos: Pos | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    location_name: LocationName | None = field(
        default=None,
        metadata={
            "name": "locationName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    location_reference: LocationReference | None = field(
        default=None,
        metadata={
            "name": "locationReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    priority_location: PriorityLocation | None = field(
        default=None,
        metadata={
            "name": "priorityLocation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    location: Location | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    status_reference: StatusReference | None = field(
        default=None,
        metadata={
            "name": "statusReference",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
