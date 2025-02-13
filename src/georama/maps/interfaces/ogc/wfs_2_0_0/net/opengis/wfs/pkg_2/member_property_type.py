from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from wfs_2_0_0.net.opengis.wfs.pkg_2.bounded_by import BoundedBy
from wfs_2_0_0.net.opengis.wfs.pkg_2.non_negative_integer_or_unknown_value import (
    NonNegativeIntegerOrUnknownValue,
)
from wfs_2_0_0.net.opengis.wfs.pkg_2.state_value_type_value import StateValueTypeValue
from wfs_2_0_0.net.opengis.wfs.pkg_2.truncated_response import TruncatedResponse
from wfs_2_0_0.org.w3.pkg_1999.xlink.actuate_type import ActuateType
from wfs_2_0_0.org.w3.pkg_1999.xlink.show_type import ShowType
from wfs_2_0_0.org.w3.pkg_1999.xlink.type_type import TypeType
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class MemberPropertyType:
    state: Optional[Union[str, StateValueTypeValue]] = field(
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
    truncated_response: Optional[TruncatedResponse] = field(
        default=None,
        metadata={
            "name": "truncatedResponse",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Attribute",
            "required": True,
        },
    )
    number_matched: Optional[Union[int, NonNegativeIntegerOrUnknownValue]] = field(
        default=None,
        metadata={
            "name": "numberMatched",
            "type": "Attribute",
            "required": True,
        },
    )
    number_returned: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberReturned",
            "type": "Attribute",
            "required": True,
        },
    )
    next: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    previous: Optional[str] = field(
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
    bounded_by: Optional[BoundedBy] = field(
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
    truncated_response: Optional[TruncatedResponse] = field(
        default=None,
        metadata={
            "name": "truncatedResponse",
            "type": "Element",
            "namespace": "http://www.opengis.net/wfs/2.0",
        },
    )
    time_stamp: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeStamp",
            "type": "Attribute",
            "required": True,
        },
    )
    number_matched: Optional[Union[int, NonNegativeIntegerOrUnknownValue]] = field(
        default=None,
        metadata={
            "name": "numberMatched",
            "type": "Attribute",
            "required": True,
        },
    )
    number_returned: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberReturned",
            "type": "Attribute",
            "required": True,
        },
    )
    next: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    previous: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lock_id: Optional[str] = field(
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

    value_collection: Optional[ValueCollection] = field(
        default=None,
        metadata={
            "name": "ValueCollection",
            "type": "Element",
        },
    )
    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
        },
    )
    simple_feature_collection: Optional[SimpleFeatureCollection] = field(
        default=None,
        metadata={
            "name": "SimpleFeatureCollection",
            "type": "Element",
        },
    )


@dataclass
class AdditionalValues:
    class Meta:
        name = "additionalValues"
        namespace = "http://www.opengis.net/wfs/2.0"

    value_collection: Optional[ValueCollection] = field(
        default=None,
        metadata={
            "name": "ValueCollection",
            "type": "Element",
        },
    )
    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
        },
    )
    simple_feature_collection: Optional[SimpleFeatureCollection] = field(
        default=None,
        metadata={
            "name": "SimpleFeatureCollection",
            "type": "Element",
        },
    )
