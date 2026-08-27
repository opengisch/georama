from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_primitive_type import (
    RelatedTimeType,
    TimeNodePropertyType,
    TimePeriodPropertyType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType
from georama.maps.interfaces.opengis.filter_1_1_0.reference_type import ReferenceType
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalEraType(DefinitionType):
    """Ordinal temporal reference systems are often hierarchically structured such
    that an ordinal era at a given level of the hierarchy includes a sequence of
    shorter, coterminous ordinal eras.

    This captured using the member/group properties. Note that in this
    schema, TIme Ordinal Era is patterned on TimeEdge, which is a
    variation from ISO 19108. This is in order to fulfill the
    requirements of ordinal reference systems based on eras delimited by
    named points or nodes, which are common in geology, archeology, etc.
    This change is subject of a change proposal to ISO

    :ivar related_time:
    :ivar start:
    :ivar end:
    :ivar extent:
    :ivar member: An Era may be composed of several member Eras. The
        "member" element implements the association to the Era at the
        next level down the hierarchy.  "member" follows the standard
        GML property pattern whereby its (complex) value may be either
        described fully inline, or may be the target of a link carried
        on the member element and described fully elsewhere, either in
        the same document or from another service.
    :ivar group: In a particular Time System, an Era may be a member of
        a group.  The "group" element implements the back-pointer to the
        Era at the next level up in the hierarchy. If the hierarchy is
        represented by describing the nested components fully in the
        their nested position inside "member" elements, then the parent
        can be easily inferred, so the group property is unnecessary.
        However, if the hierarchy is represented by links carried on the
        "member" property elements, pointing to Eras described fully
        elsewhere, then it may be useful for a child (member) era to
        carry an explicit pointer back to its parent (group) Era.
    """

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
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeOrdinalEraPropertyType:
    time_ordinal_era: TimeOrdinalEra | None = field(
        default=None,
        metadata={
            "name": "TimeOrdinalEra",
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
