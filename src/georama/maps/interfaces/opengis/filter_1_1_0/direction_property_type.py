from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.code_type import CodeType
from georama.maps.interfaces.opengis.filter_1_1_0.compass_point import CompassPoint
from georama.maps.interfaces.opengis.filter_1_1_0.direction_vector import (
    DirectionVector,
)
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.string_or_ref_type import (
    StringOrRefType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DirectionPropertyType:
    direction_vector: Optional[DirectionVector] = field(
        default=None,
        metadata={
            "name": "DirectionVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    compass_point: Optional[CompassPoint] = field(
        default=None,
        metadata={
            "name": "CompassPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    direction_keyword: Optional[CodeType] = field(
        default=None,
        metadata={
            "name": "DirectionKeyword",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    direction_string: Optional[StringOrRefType] = field(
        default=None,
        metadata={
            "name": "DirectionString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
