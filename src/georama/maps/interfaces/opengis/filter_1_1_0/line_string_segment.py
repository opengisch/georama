from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.line_string_segment_type import (
    LineStringSegmentType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineStringSegment(LineStringSegmentType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
