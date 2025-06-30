from dataclasses import dataclass, field
from typing import ForwardRef, Union

from georama.maps.interfaces.ogc.wfs_2_0_0.after import After
from georama.maps.interfaces.ogc.wfs_2_0_0.any_interacts import AnyInteracts
from georama.maps.interfaces.ogc.wfs_2_0_0.bbox import Bbox
from georama.maps.interfaces.ogc.wfs_2_0_0.before import Before
from georama.maps.interfaces.ogc.wfs_2_0_0.begins import Begins
from georama.maps.interfaces.ogc.wfs_2_0_0.begun_by import BegunBy
from georama.maps.interfaces.ogc.wfs_2_0_0.beyond import Beyond
from georama.maps.interfaces.ogc.wfs_2_0_0.contains import Contains
from georama.maps.interfaces.ogc.wfs_2_0_0.crosses import Crosses
from georama.maps.interfaces.ogc.wfs_2_0_0.disjoint import Disjoint
from georama.maps.interfaces.ogc.wfs_2_0_0.during import During
from georama.maps.interfaces.ogc.wfs_2_0_0.dwithin import Dwithin
from georama.maps.interfaces.ogc.wfs_2_0_0.ended_by import EndedBy
from georama.maps.interfaces.ogc.wfs_2_0_0.ends import Ends
from georama.maps.interfaces.ogc.wfs_2_0_0.equals import Equals
from georama.maps.interfaces.ogc.wfs_2_0_0.function_type import Function
from georama.maps.interfaces.ogc.wfs_2_0_0.intersects import Intersects
from georama.maps.interfaces.ogc.wfs_2_0_0.logic_ops_type import LogicOpsType
from georama.maps.interfaces.ogc.wfs_2_0_0.meets import Meets
from georama.maps.interfaces.ogc.wfs_2_0_0.met_by import MetBy
from georama.maps.interfaces.ogc.wfs_2_0_0.overlapped_by import OverlappedBy
from georama.maps.interfaces.ogc.wfs_2_0_0.overlaps import Overlaps
from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_between import PropertyIsBetween
from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_equal_to import PropertyIsEqualTo
from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_greater_than import (
    PropertyIsGreaterThan,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_greater_than_or_equal_to import (
    PropertyIsGreaterThanOrEqualTo,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_less_than import (
    PropertyIsLessThan,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_less_than_or_equal_to import (
    PropertyIsLessThanOrEqualTo,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_like import PropertyIsLike
from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_nil import PropertyIsNil
from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_not_equal_to import (
    PropertyIsNotEqualTo,
)
from georama.maps.interfaces.ogc.wfs_2_0_0.property_is_null import PropertyIsNull
from georama.maps.interfaces.ogc.wfs_2_0_0.resource_id import ResourceId
from georama.maps.interfaces.ogc.wfs_2_0_0.tcontains import Tcontains
from georama.maps.interfaces.ogc.wfs_2_0_0.tequals import Tequals
from georama.maps.interfaces.ogc.wfs_2_0_0.touches import Touches
from georama.maps.interfaces.ogc.wfs_2_0_0.toverlaps import Toverlaps
from georama.maps.interfaces.ogc.wfs_2_0_0.within import Within

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class BinaryLogicOpType(LogicOpsType):
    choice: list[
        Union[
            PropertyIsBetween,
            PropertyIsNil,
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
            AnyInteracts,
            OverlappedBy,
            Toverlaps,
            MetBy,
            Meets,
            Tequals,
            Ends,
            EndedBy,
            During,
            Tcontains,
            BegunBy,
            Begins,
            Before,
            After,
            "Not",
            "Or",
            "And",
            Function,
            ResourceId,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PropertyIsBetween",
                    "type": PropertyIsBetween,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsNil",
                    "type": PropertyIsNil,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsNull",
                    "type": PropertyIsNull,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsLike",
                    "type": PropertyIsLike,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsGreaterThanOrEqualTo",
                    "type": PropertyIsGreaterThanOrEqualTo,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsLessThanOrEqualTo",
                    "type": PropertyIsLessThanOrEqualTo,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsGreaterThan",
                    "type": PropertyIsGreaterThan,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsLessThan",
                    "type": PropertyIsLessThan,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsNotEqualTo",
                    "type": PropertyIsNotEqualTo,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsEqualTo",
                    "type": PropertyIsEqualTo,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "BBOX",
                    "type": Bbox,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Beyond",
                    "type": Beyond,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "DWithin",
                    "type": Dwithin,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Contains",
                    "type": Contains,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Intersects",
                    "type": Intersects,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Crosses",
                    "type": Crosses,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Overlaps",
                    "type": Overlaps,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Within",
                    "type": Within,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Touches",
                    "type": Touches,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Disjoint",
                    "type": Disjoint,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Equals",
                    "type": Equals,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "AnyInteracts",
                    "type": AnyInteracts,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "OverlappedBy",
                    "type": OverlappedBy,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "TOverlaps",
                    "type": Toverlaps,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "MetBy",
                    "type": MetBy,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Meets",
                    "type": Meets,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "TEquals",
                    "type": Tequals,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Ends",
                    "type": Ends,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "EndedBy",
                    "type": EndedBy,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "During",
                    "type": During,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "TContains",
                    "type": Tcontains,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "BegunBy",
                    "type": BegunBy,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Begins",
                    "type": Begins,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Before",
                    "type": Before,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "After",
                    "type": After,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Not",
                    "type": ForwardRef("Not"),
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Or",
                    "type": ForwardRef("Or"),
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "And",
                    "type": ForwardRef("And"),
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Function",
                    "type": Function,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "ResourceId",
                    "type": ResourceId,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
            ),
        },
    )


@dataclass
class And(BinaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"


@dataclass
class Or(BinaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"


@dataclass
class UnaryLogicOpType(LogicOpsType):
    choice: list[
        Union[
            PropertyIsBetween,
            PropertyIsNil,
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
            AnyInteracts,
            OverlappedBy,
            Toverlaps,
            MetBy,
            Meets,
            Tequals,
            Ends,
            EndedBy,
            During,
            Tcontains,
            BegunBy,
            Begins,
            Before,
            After,
            "Not",
            Or,
            And,
            Function,
            ResourceId,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PropertyIsBetween",
                    "type": PropertyIsBetween,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsNil",
                    "type": PropertyIsNil,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsNull",
                    "type": PropertyIsNull,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsLike",
                    "type": PropertyIsLike,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsGreaterThanOrEqualTo",
                    "type": PropertyIsGreaterThanOrEqualTo,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsLessThanOrEqualTo",
                    "type": PropertyIsLessThanOrEqualTo,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsGreaterThan",
                    "type": PropertyIsGreaterThan,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsLessThan",
                    "type": PropertyIsLessThan,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsNotEqualTo",
                    "type": PropertyIsNotEqualTo,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "PropertyIsEqualTo",
                    "type": PropertyIsEqualTo,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "BBOX",
                    "type": Bbox,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Beyond",
                    "type": Beyond,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "DWithin",
                    "type": Dwithin,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Contains",
                    "type": Contains,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Intersects",
                    "type": Intersects,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Crosses",
                    "type": Crosses,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Overlaps",
                    "type": Overlaps,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Within",
                    "type": Within,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Touches",
                    "type": Touches,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Disjoint",
                    "type": Disjoint,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Equals",
                    "type": Equals,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "AnyInteracts",
                    "type": AnyInteracts,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "OverlappedBy",
                    "type": OverlappedBy,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "TOverlaps",
                    "type": Toverlaps,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "MetBy",
                    "type": MetBy,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Meets",
                    "type": Meets,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "TEquals",
                    "type": Tequals,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Ends",
                    "type": Ends,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "EndedBy",
                    "type": EndedBy,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "During",
                    "type": During,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "TContains",
                    "type": Tcontains,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "BegunBy",
                    "type": BegunBy,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Begins",
                    "type": Begins,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Before",
                    "type": Before,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "After",
                    "type": After,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Not",
                    "type": ForwardRef("Not"),
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Or",
                    "type": Or,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "And",
                    "type": And,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "Function",
                    "type": Function,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
                {
                    "name": "ResourceId",
                    "type": ResourceId,
                    "namespace": "http://www.opengis.net/fes/2.0",
                },
            ),
        },
    )


@dataclass
class Not(UnaryLogicOpType):
    class Meta:
        namespace = "http://www.opengis.net/fes/2.0"
