from dataclasses import dataclass, field
from typing import ForwardRef, Union

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
    choice: list[
        Union[
            PropertyIsBetween,
            PropertyIsNull,
            PropertyIsLike,
            PropertyIsGreaterThanOrEqualTo,
            PropertyIsLessThanOrEqualTo,
            PropertyIsGreaterThan,
            PropertyIsLessThan,
            PropertyIsNotEqualTo,
            PropertyIsEqualTo,
            Bbox,
            Beyond,
            Dwithin,
            Contains,
            Intersects,
            Crosses,
            Overlaps,
            Within,
            Touches,
            Disjoint,
            Equals,
            "Not",
            "Or",
            "And",
            Function,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PropertyIsBetween",
                    "type": PropertyIsBetween,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsNull",
                    "type": PropertyIsNull,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsLike",
                    "type": PropertyIsLike,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsGreaterThanOrEqualTo",
                    "type": PropertyIsGreaterThanOrEqualTo,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsLessThanOrEqualTo",
                    "type": PropertyIsLessThanOrEqualTo,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsGreaterThan",
                    "type": PropertyIsGreaterThan,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsLessThan",
                    "type": PropertyIsLessThan,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsNotEqualTo",
                    "type": PropertyIsNotEqualTo,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsEqualTo",
                    "type": PropertyIsEqualTo,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "BBOX",
                    "type": Bbox,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Beyond",
                    "type": Beyond,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "DWithin",
                    "type": Dwithin,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Contains",
                    "type": Contains,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Intersects",
                    "type": Intersects,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Crosses",
                    "type": Crosses,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Overlaps",
                    "type": Overlaps,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Within",
                    "type": Within,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Touches",
                    "type": Touches,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Disjoint",
                    "type": Disjoint,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Equals",
                    "type": Equals,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Not",
                    "type": ForwardRef("Not"),
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Or",
                    "type": ForwardRef("Or"),
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "And",
                    "type": ForwardRef("And"),
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Function",
                    "type": Function,
                    "namespace": "http://www.opengis.net/ogc",
                },
            ),
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
    choice: (
        Union[
            PropertyIsBetween,
            PropertyIsNull,
            PropertyIsLike,
            PropertyIsGreaterThanOrEqualTo,
            PropertyIsLessThanOrEqualTo,
            PropertyIsGreaterThan,
            PropertyIsLessThan,
            PropertyIsNotEqualTo,
            PropertyIsEqualTo,
            Bbox,
            Beyond,
            Dwithin,
            Contains,
            Intersects,
            Crosses,
            Overlaps,
            Within,
            Touches,
            Disjoint,
            Equals,
            "Not",
            Or,
            And,
            Function,
        ]
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PropertyIsBetween",
                    "type": PropertyIsBetween,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsNull",
                    "type": PropertyIsNull,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsLike",
                    "type": PropertyIsLike,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsGreaterThanOrEqualTo",
                    "type": PropertyIsGreaterThanOrEqualTo,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsLessThanOrEqualTo",
                    "type": PropertyIsLessThanOrEqualTo,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsGreaterThan",
                    "type": PropertyIsGreaterThan,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsLessThan",
                    "type": PropertyIsLessThan,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsNotEqualTo",
                    "type": PropertyIsNotEqualTo,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyIsEqualTo",
                    "type": PropertyIsEqualTo,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "BBOX",
                    "type": Bbox,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Beyond",
                    "type": Beyond,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "DWithin",
                    "type": Dwithin,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Contains",
                    "type": Contains,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Intersects",
                    "type": Intersects,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Crosses",
                    "type": Crosses,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Overlaps",
                    "type": Overlaps,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Within",
                    "type": Within,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Touches",
                    "type": Touches,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Disjoint",
                    "type": Disjoint,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Equals",
                    "type": Equals,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Not",
                    "type": ForwardRef("Not"),
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Or",
                    "type": Or,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "And",
                    "type": And,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Function",
                    "type": Function,
                    "namespace": "http://www.opengis.net/ogc",
                },
            ),
        },
    )


@dataclass
class Not(UnaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
