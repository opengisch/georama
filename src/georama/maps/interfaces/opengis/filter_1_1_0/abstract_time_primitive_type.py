from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_object_type import (
    AbstractTimeObjectType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.duration import Duration
from georama.maps.interfaces.opengis.filter_1_1_0.reference_type import ReferenceType
from georama.maps.interfaces.opengis.filter_1_1_0.related_time_type_relative_position import (
    RelatedTimeTypeRelativePosition,
)
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.time_interval import TimeInterval
from georama.maps.interfaces.opengis.filter_1_1_0.time_position import TimePosition
from georama.maps.interfaces.opengis.filter_1_1_0.time_position_type import (
    TimePositionType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimePrimitiveType(AbstractTimeObjectType):
    """
    The abstract supertype for temporal primitives.
    """

    related_time: list["RelatedTimeType"] = field(
        default_factory=list,
        metadata={
            "name": "relatedTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class AbstractTimeGeometricPrimitiveType(AbstractTimePrimitiveType):
    """The abstract supertype for temporal geometric primitives.

    A temporal geometry must be associated with a temporal reference
    system via URI. The Gregorian calendar with UTC is the default
    reference system, following ISO 8601. Other reference systems in
    common use include the GPS calendar and the Julian calendar.
    """

    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AbstractTimeTopologyPrimitiveType(AbstractTimePrimitiveType):
    """
    The element "complex" carries a reference to the complex containing this
    primitive.
    """

    complex: ReferenceType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class TimeInstantType(AbstractTimeGeometricPrimitiveType):
    """
    Omit back-pointers begunBy, endedBy.
    """

    time_position: TimePosition | None = field(
        default=None,
        metadata={
            "name": "timePosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class TimeInstant(TimeInstantType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeInstantPropertyType:
    time_instant: TimeInstant | None = field(
        default=None,
        metadata={
            "name": "TimeInstant",
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


@dataclass
class TimeNodeType(AbstractTimeTopologyPrimitiveType):
    """
    Type declaration of the element "TimeNode".
    """

    previous_edge: list["TimeEdgePropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "previousEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    next_edge: list["TimeEdgePropertyType"] = field(
        default_factory=list,
        metadata={
            "name": "nextEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    position: TimeInstantPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class TimePeriodType(AbstractTimeGeometricPrimitiveType):
    begin_position_or_begin: TimePositionType | TimeInstantPropertyType | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "beginPosition",
                    "type": TimePositionType,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "begin",
                    "type": TimeInstantPropertyType,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    end_position_or_end: TimePositionType | TimeInstantPropertyType | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "endPosition",
                    "type": TimePositionType,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "end",
                    "type": TimeInstantPropertyType,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    duration_or_time_interval: Duration | TimeInterval | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "duration",
                    "type": Duration,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "timeInterval",
                    "type": TimeInterval,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )


@dataclass
class TimeNode(TimeNodeType):
    """ "TimeNode" is a zero dimensional temporal topology primitive, expresses a
    position in topological time, and is a start and an end of time edge, which
    represents states of time.

    Time node may be isolated. However, it cannot describe the ordering
    relationships with other primitives. An isolated node may not be an
    element of any temporal topology complex.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimePeriod(TimePeriodType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeNodePropertyType:
    """A time node property can either be any time node element encapsulated in an
    element of this type or an XLink reference to a remote time node element (where
    remote includes elements located elsewhere in the same document).

    Note that either the reference or the contained element must be
    given, but not both or none.
    """

    time_node: TimeNode | None = field(
        default=None,
        metadata={
            "name": "TimeNode",
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


@dataclass
class TimePeriodPropertyType:
    time_period: TimePeriod | None = field(
        default=None,
        metadata={
            "name": "TimePeriod",
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


@dataclass
class TimeEdgeType(AbstractTimeTopologyPrimitiveType):
    """
    Type declaration of the element "TimeEdge".
    """

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


@dataclass
class TimeEdge(TimeEdgeType):
    """TimeEdge is one dimensional temporal topology primitive, expresses a state
    in topological time.

    It has an orientation from its start toward the end, and its
    boundaries shall associate with two different time nodes.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TimeEdgePropertyType:
    """A time edge property can either be any time edge element encapsulated in an
    element of this type or an XLink reference to a remote time edge element (where
    remote includes elements located elsewhere in the same document).

    Note that either the reference or the contained element must be
    given, but not both or none.
    """

    time_edge: TimeEdge | None = field(
        default=None,
        metadata={
            "name": "TimeEdge",
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


@dataclass
class TimePrimitivePropertyType:
    choice: TimeEdge | TimeNode | TimePeriod | TimeInstant | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeEdge",
                    "type": TimeEdge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeNode",
                    "type": TimeNode,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimePeriod",
                    "type": TimePeriod,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeInstant",
                    "type": TimeInstant,
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


@dataclass
class RelatedTimeType(TimePrimitivePropertyType):
    relative_position: RelatedTimeTypeRelativePosition | None = field(
        default=None,
        metadata={
            "name": "relativePosition",
            "type": "Attribute",
        },
    )
