from dataclasses import dataclass, field

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
    choice: DirectionVector | CompassPoint | CodeType | StringOrRefType | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DirectionVector",
                    "type": DirectionVector,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompassPoint",
                    "type": CompassPoint,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectionKeyword",
                    "type": CodeType,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectionString",
                    "type": StringOrRefType,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
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
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: str | None = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )
