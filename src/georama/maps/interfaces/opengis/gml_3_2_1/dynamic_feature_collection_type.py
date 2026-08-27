from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_feature_member_type import (
    AbstractFeatureMemberType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.dynamic_feature import DynamicFeature
from georama.maps.interfaces.opengis.gml_3_2_1.dynamic_feature_type import (
    DynamicFeatureType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DynamicFeatureCollectionType(DynamicFeatureType):
    dynamic_members: Optional["DynamicMembers"] = field(
        default=None,
        metadata={
            "name": "dynamicMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class DynamicFeatureCollection(DynamicFeatureCollectionType):
    """A gml:DynamicFeatureCollection is a feature collection that has a
    gml:validTime property (i.e. is a snapshot of the feature collection) or which
    has a gml:history property that contains one or more gml:AbstractTimeSlices
    each of which contain values of the time varying properties of the feature
    collection.

    Note that the gml:DynamicFeatureCollection may be one of the following:
    1.      A feature collection which consists of static feature members (members do not change in time) but which has properties of the collection object as a whole that do change in time .
    2.      A feature collection which consists of dynamic feature members (the members are gml:DynamicFeatures) but which also has properties of the collection as a whole that vary in time.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DynamicFeatureMemberType(AbstractFeatureMemberType):
    dynamic_feature_collection: list[DynamicFeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature: list[DynamicFeature] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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


@dataclass
class DynamicMembers(DynamicFeatureMemberType):
    class Meta:
        name = "dynamicMembers"
        namespace = "http://www.opengis.net/gml/3.2"
