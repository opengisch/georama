from dataclasses import dataclass, field
from typing import List

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.line_string_segment import (
    LineStringSegment,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class LineStringSegmentArrayPropertyType:
    """
    Gml:LineStringSegmentArrayPropertyType provides a container for line strings.
    """

    line_string_segment: List[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
