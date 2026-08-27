from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.bounding_box import BoundingBox
from georama.maps.interfaces.opengis.filter_1_1_0.bounding_polygon import (
    BoundingPolygon,
)
from georama.maps.interfaces.opengis.filter_1_1_0.description import Description
from georama.maps.interfaces.opengis.filter_1_1_0.temporal_extent import TemporalExtent
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_extent import VerticalExtent

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ExtentType:
    """Information about the spatial, vertical, and/or temporal extent of a
    reference system object.

    Constraints: At least one of the elements "description", "boundingBox", "boundingPolygon", "verticalExtent", and temporalExtent" must be included, but more that one can be included when appropriate. Furthermore, more than one "boundingBox", "boundingPolygon", "verticalExtent", and/or temporalExtent" element can be included, with more than one meaning the union of the individual domains.

    :ivar description: Description of spatial and/or temporal extent of
        this object.
    :ivar bounding_box_or_bounding_polygon:
    :ivar vertical_extent: Unordered list of vertical intervals whose
        union describes the spatial domain of this object.
    :ivar temporal_extent: Unordered list of time periods whose union
        describes the spatial domain of this object.
    """

    description: Description | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bounding_box_or_bounding_polygon: list[BoundingBox | BoundingPolygon] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "boundingBox",
                    "type": BoundingBox,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "boundingPolygon",
                    "type": BoundingPolygon,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    vertical_extent: list[VerticalExtent] = field(
        default_factory=list,
        metadata={
            "name": "verticalExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_extent: list[TemporalExtent] = field(
        default_factory=list,
        metadata={
            "name": "temporalExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
