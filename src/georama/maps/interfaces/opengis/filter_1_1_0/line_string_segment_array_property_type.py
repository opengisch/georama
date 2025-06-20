from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.line_string_segment import (
    LineStringSegment,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineStringSegmentArrayPropertyType:
    line_string_segment: list[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
