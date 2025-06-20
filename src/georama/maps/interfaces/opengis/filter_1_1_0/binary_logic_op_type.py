from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.bbox import Bbox
from georama.maps.interfaces.opengis.filter_1_1_0.beyond import Beyond
from georama.maps.interfaces.opengis.filter_1_1_0.binary_operator_type import Function
from georama.maps.interfaces.opengis.filter_1_1_0.contains import Contains
from georama.maps.interfaces.opengis.filter_1_1_0.crosses import Crosses
from georama.maps.interfaces.opengis.filter_1_1_0.disjoint import Disjoint
from georama.maps.interfaces.opengis.filter_1_1_0.dwithin import Dwithin
from georama.maps.interfaces.opengis.filter_1_1_0.equals import Equals
from georama.maps.interfaces.opengis.filter_1_1_0.intersects import Intersects
from georama.maps.interfaces.opengis.filter_1_1_0.logic_ops_type import LogicOpsType
from georama.maps.interfaces.opengis.filter_1_1_0.overlaps import Overlaps
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_between import (
    PropertyIsBetween,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_equal_to import (
    PropertyIsEqualTo,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_greater_than import (
    PropertyIsGreaterThan,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_greater_than_or_equal_to import (
    PropertyIsGreaterThanOrEqualTo,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_less_than import (
    PropertyIsLessThan,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_less_than_or_equal_to import (
    PropertyIsLessThanOrEqualTo,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_like import PropertyIsLike
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_not_equal_to import (
    PropertyIsNotEqualTo,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_is_null import PropertyIsNull
from georama.maps.interfaces.opengis.filter_1_1_0.touches import Touches
from georama.maps.interfaces.opengis.filter_1_1_0.within import Within

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class BinaryLogicOpType(LogicOpsType):
    property_is_between: list[PropertyIsBetween] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsBetween",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_null: list[PropertyIsNull] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_like: list[PropertyIsLike] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_greater_than_or_equal_to: list[PropertyIsGreaterThanOrEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_less_than_or_equal_to: list[PropertyIsLessThanOrEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_greater_than: list[PropertyIsGreaterThan] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_less_than: list[PropertyIsLessThan] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_not_equal_to: list[PropertyIsNotEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_equal_to: list[PropertyIsEqualTo] = field(
        default_factory=list,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    bbox: list[Bbox] = field(
        default_factory=list,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    beyond: list[Beyond] = field(
        default_factory=list,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    dwithin: list[Dwithin] = field(
        default_factory=list,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    contains: list[Contains] = field(
        default_factory=list,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    intersects: list[Intersects] = field(
        default_factory=list,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    crosses: list[Crosses] = field(
        default_factory=list,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    overlaps: list[Overlaps] = field(
        default_factory=list,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    within: list[Within] = field(
        default_factory=list,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    touches: list[Touches] = field(
        default_factory=list,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    disjoint: list[Disjoint] = field(
        default_factory=list,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    equals: list[Equals] = field(
        default_factory=list,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    not_value: list["Not"] = field(
        default_factory=list,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    or_value: list["Or"] = field(
        default_factory=list,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    and_value: list["And"] = field(
        default_factory=list,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    function: list[Function] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "min_occurs": 2,
        },
    )


@dataclass
class And(BinaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Or(BinaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class UnaryLogicOpType(LogicOpsType):
    property_is_between: Optional[PropertyIsBetween] = field(
        default=None,
        metadata={
            "name": "PropertyIsBetween",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_null: Optional[PropertyIsNull] = field(
        default=None,
        metadata={
            "name": "PropertyIsNull",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_like: Optional[PropertyIsLike] = field(
        default=None,
        metadata={
            "name": "PropertyIsLike",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_greater_than_or_equal_to: Optional[PropertyIsGreaterThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_less_than_or_equal_to: Optional[PropertyIsLessThanOrEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThanOrEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_greater_than: Optional[PropertyIsGreaterThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsGreaterThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_less_than: Optional[PropertyIsLessThan] = field(
        default=None,
        metadata={
            "name": "PropertyIsLessThan",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_not_equal_to: Optional[PropertyIsNotEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsNotEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_is_equal_to: Optional[PropertyIsEqualTo] = field(
        default=None,
        metadata={
            "name": "PropertyIsEqualTo",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    bbox: Optional[Bbox] = field(
        default=None,
        metadata={
            "name": "BBOX",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    beyond: Optional[Beyond] = field(
        default=None,
        metadata={
            "name": "Beyond",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    dwithin: Optional[Dwithin] = field(
        default=None,
        metadata={
            "name": "DWithin",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    contains: Optional[Contains] = field(
        default=None,
        metadata={
            "name": "Contains",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    intersects: Optional[Intersects] = field(
        default=None,
        metadata={
            "name": "Intersects",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    crosses: Optional[Crosses] = field(
        default=None,
        metadata={
            "name": "Crosses",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    overlaps: Optional[Overlaps] = field(
        default=None,
        metadata={
            "name": "Overlaps",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    within: Optional[Within] = field(
        default=None,
        metadata={
            "name": "Within",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    touches: Optional[Touches] = field(
        default=None,
        metadata={
            "name": "Touches",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    disjoint: Optional[Disjoint] = field(
        default=None,
        metadata={
            "name": "Disjoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    equals: Optional[Equals] = field(
        default=None,
        metadata={
            "name": "Equals",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    not_value: Optional["Not"] = field(
        default=None,
        metadata={
            "name": "Not",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    or_value: Optional[Or] = field(
        default=None,
        metadata={
            "name": "Or",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    and_value: Optional[And] = field(
        default=None,
        metadata={
            "name": "And",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    function: Optional[Function] = field(
        default=None,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )


@dataclass
class Not(UnaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
