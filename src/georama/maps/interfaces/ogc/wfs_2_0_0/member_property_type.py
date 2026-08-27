from dataclasses import dataclass, field
from typing import ForwardRef, Optional

from xsdata.models.datatype import XmlDateTime

from georama.maps.interfaces.ogc.wfs_2_0_0.actuate_type import ActuateType
from georama.maps.interfaces.ogc.wfs_2_0_0.bounded_by import BoundedBy
from georama.maps.interfaces.ogc.wfs_2_0_0.non_negative_integer_or_unknown_value import (
    NonNegativeIntegerOrUnknownValue,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.show_type import ShowType
from georama.maps.interfaces.ogc.wfs_2_0_0.state_value_type_value import (
    StateValueTypeValue,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.truncated_response import TruncatedResponse
from georama.maps.interfaces.ogc.wfs_2_0_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class MemberPropertyType:
    state: str | StateValueTypeValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
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
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "Tuple",
                    "type": ForwardRef("Tuple"),
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
                {
                    "name": "FeatureCollection",
                    "type": ForwardRef("FeatureCollection"),
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
                {
                    "name": "SimpleFeatureCollection",
                    "type": ForwardRef("SimpleFeatureCollection"),
                    "namespace": "http://www.opengis.net/wfs/2.0",
                },
            ),
        },
    )


@dataclass
class ValueCollectionType:
    member: list["Member"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    additional_values: Optional["AdditionalValues"] = field(
        default=None,
        metadata={
            "name": "additionalValues",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    truncated_response: TruncatedResponse | None = field(
        default=None,
        metadata={
            "name": "truncatedResponse",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    time_stamp: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Attribute",
            "required": True,
        },
    )
    number_matched: int | NonNegativeIntegerOrUnknownValue | None = field(
        default=None,
        metadata={
            "name": "numberMatched",
            "type": "Attribute",
            "required": True,
        },
    )
    number_returned: int | None = field(
        default=None,
        metadata={
            "name": "numberReturned",
            "type": "Attribute",
            "required": True,
        },
    )
    next: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    previous: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class ValueCollection(ValueCollectionType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"


@dataclass
class Member(MemberPropertyType):
    class Meta:
        name = "member"
        namespace = "http://www.opengis.net/wfs/2.0"


@dataclass
class SimpleFeatureCollectionType:
    bounded_by: BoundedBy | None = field(
        default=None,
        metadata={
            "name": "boundedBy",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    member: list[Member] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )


@dataclass
class TupleType:
    member: list[Member] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
            "min_occurs": 2,
        },
    )


@dataclass
class FeatureCollectionType(SimpleFeatureCollectionType):
    additional_objects: Optional["AdditionalObjects"] = field(
        default=None,
        metadata={
            "name": "additionalObjects",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    truncated_response: TruncatedResponse | None = field(
        default=None,
        metadata={
            "name": "truncatedResponse",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    time_stamp: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Attribute",
            "required": True,
        },
    )
    number_matched: int | NonNegativeIntegerOrUnknownValue | None = field(
        default=None,
        metadata={
            "name": "numberMatched",
            "type": "Attribute",
            "required": True,
        },
    )
    number_returned: int | None = field(
        default=None,
        metadata={
            "name": "numberReturned",
            "type": "Attribute",
            "required": True,
        },
    )
    next: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    previous: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lock_id: str | None = field(
        default=None,
        metadata={
            "name": "lockId",
            "type": "Attribute",
        },
    )


@dataclass
class SimpleFeatureCollection(SimpleFeatureCollectionType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"


@dataclass
class Tuple(TupleType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"


@dataclass
class FeatureCollection(FeatureCollectionType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"


@dataclass
class AdditionalObjects:
    class Meta:
        name = "additionalObjects"
        namespace = "http://www.opengis.net/wfs/2.0"

    value_collection_or_feature_collection_or_simple_feature_collection: (
        ValueCollection | FeatureCollection | SimpleFeatureCollection | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ValueCollection",
                    "type": ValueCollection,
                },
                {
                    "name": "FeatureCollection",
                    "type": FeatureCollection,
                },
                {
                    "name": "SimpleFeatureCollection",
                    "type": SimpleFeatureCollection,
                },
            ),
        },
    )


@dataclass
class AdditionalValues:
    class Meta:
        name = "additionalValues"
        namespace = "http://www.opengis.net/wfs/2.0"

    value_collection_or_feature_collection_or_simple_feature_collection: (
        ValueCollection | FeatureCollection | SimpleFeatureCollection | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ValueCollection",
                    "type": ValueCollection,
                },
                {
                    "name": "FeatureCollection",
                    "type": FeatureCollection,
                },
                {
                    "name": "SimpleFeatureCollection",
                    "type": SimpleFeatureCollection,
                },
            ),
        },
    )
