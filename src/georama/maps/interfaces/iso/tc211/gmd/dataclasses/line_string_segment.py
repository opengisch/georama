from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.line_string_segment_type import (
    LineStringSegmentType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineStringSegment(LineStringSegmentType):
    """A LineStringSegment is a curve segment that is defined by two or more
    control points including the start and end point, with linear interpolation
    between them.

    The content model follows the general pattern for the encoding of
    curve segments.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
