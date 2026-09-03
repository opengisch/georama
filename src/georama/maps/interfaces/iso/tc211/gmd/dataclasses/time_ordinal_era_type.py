from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_time_primitive_type import (
    RelatedTimeType,
    TimeNodePropertyType,
    TimePeriodPropertyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_type import (
    DefinitionType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.reference_type import (
    ReferenceType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalEraType(DefinitionType):
    related_time: list[RelatedTimeType] = field(
        default_factory=list,
        metadata={
            "name": "relatedTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    start: TimeNodePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    end: TimeNodePropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    extent: TimePeriodPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    member: list["TimeOrdinalEraPropertyType"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    group: ReferenceType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class TimeOrdinalEra(TimeOrdinalEraType):
    """Its content model follows the pattern of gml:TimeEdge, inheriting standard
    properties from gml:DefinitionType, and adding gml:start, gml:end and
    gml:extent properties, a set of gml:member properties which indicate ordered
    gml:TimeOrdinalEra elements, and a gml:group property which points to the
    parent era.

    The recursive inclusion of gml:TimeOrdinalEra elements allow the
    construction of an arbitrary depth hierarchical ordinal reference
    schema, such that an ordinal era at a given level of the hierarchy
    includes a sequence of shorter, coterminous ordinal eras.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalEraPropertyType:
    """
    Gml:TimeOrdinalEraPropertyType provides for associating a gml:TimeOrdinalEra
    with an object.
    """

    time_ordinal_era: TimeOrdinalEra | None = field(
        default=None,
        metadata={
            "name": "TimeOrdinalEra",
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
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue | None = field(
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
            "namespace": "http://www.opengis.net/gml",
        },
    )
