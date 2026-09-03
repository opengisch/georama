from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.length_type import LengthType
from georama.maps.interfaces.opengis.gml_3_2_1.line_string_segment_array_property_type import (
    LineStringSegmentArrayPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.surface_type import SurfaceType
from georama.maps.interfaces.opengis.gml_3_2_1.tin_type_control_point import (
    TinTypeControlPoint,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TinType(SurfaceType):
    stop_lines: list[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "stopLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    break_lines: list[LineStringSegmentArrayPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "breakLines",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    max_length: LengthType | None = field(
        default=None,
        metadata={
            "name": "maxLength",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    control_point: TinTypeControlPoint | None = field(
        default=None,
        metadata={
            "name": "controlPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
