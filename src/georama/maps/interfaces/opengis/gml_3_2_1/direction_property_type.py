from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.code_type import CodeType
from georama.maps.interfaces.opengis.gml_3_2_1.compass_point_enumeration import (
    CompassPointEnumeration,
)
from georama.maps.interfaces.opengis.gml_3_2_1.direction_description_type import (
    DirectionDescriptionType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.direction_vector_type import (
    DirectionVectorType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.string_or_ref_type import StringOrRefType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectionPropertyType:
    direction_vector: DirectionVectorType | None = field(
        default=None,
        metadata={
            "name": "DirectionVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    direction_description: DirectionDescriptionType | None = field(
        default=None,
        metadata={
            "name": "DirectionDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    compass_point: CompassPointEnumeration | None = field(
        default=None,
        metadata={
            "name": "CompassPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    direction_keyword: CodeType | None = field(
        default=None,
        metadata={
            "name": "DirectionKeyword",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    direction_string: StringOrRefType | None = field(
        default=None,
        metadata={
            "name": "DirectionString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
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
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: str | None = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
