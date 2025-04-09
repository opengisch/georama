from dataclasses import dataclass, field
from typing import List, Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_feature_member_type import (
    AbstractFeatureMemberType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dynamic_feature import (
    DynamicFeature,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dynamic_feature_type import (
    DynamicFeatureType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DynamicFeatureCollectionType(DynamicFeatureType):
    dynamic_members: Optional["DynamicMembers"] = field(
        default=None,
        metadata={
            "name": "dynamicMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
        namespace = "http://www.opengis.net/gml"


@dataclass
class DynamicFeatureMemberType(AbstractFeatureMemberType):
    dynamic_feature_collection: List[DynamicFeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dynamic_feature: List[DynamicFeature] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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


@dataclass
class DynamicMembers(DynamicFeatureMemberType):
    class Meta:
        name = "dynamicMembers"
        namespace = "http://www.opengis.net/gml"
