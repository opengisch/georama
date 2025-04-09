from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.length_type import LengthType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.line_string_segment_array_property_type import (
    LineStringSegmentArrayPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.tin_type_control_point import (
    TinTypeControlPoint,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.triangulated_surface_type import (
    TriangulatedSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TinType(TriangulatedSurfaceType):
    stop_lines: List[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "stopLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    break_lines: List[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "breakLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    max_length: Optional[LengthType] = field(
        default=None,
        metadata={
            "name": "maxLength",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    control_point: Optional[TinTypeControlPoint] = field(
        default=None,
        metadata={
            "name": "controlPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
