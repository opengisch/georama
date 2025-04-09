from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_type import CodeType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.compass_point_enumeration import (
    CompassPointEnumeration,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.direction_description_type import (
    DirectionDescriptionType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.direction_vector_type import (
    DirectionVectorType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.string_or_ref_type import (
    StringOrRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DirectionPropertyType:
    direction_vector: Optional[DirectionVectorType] = field(
        default=None,
        metadata={
            "name": "DirectionVector",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    direction_description: Optional[DirectionDescriptionType] = field(
        default=None,
        metadata={
            "name": "DirectionDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    compass_point: Optional[CompassPointEnumeration] = field(
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: str = field(
        init=False,
        default="simple",
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
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
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
