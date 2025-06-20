from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.expression_type import ExpressionType
from georama.maps.interfaces.opengis.filter_1_1_0.literal import Literal
from georama.maps.interfaces.opengis.filter_1_1_0.property_name import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class BinaryOperatorType(ExpressionType):
    literal: list[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    function: list["Function"] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    property_name: list[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    div: list["Div"] = field(
        default_factory=list,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    mul: list["Mul"] = field(
        default_factory=list,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    sub: list["Sub"] = field(
        default_factory=list,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )
    add: list["Add"] = field(
        default_factory=list,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "max_occurs": 2,
        },
    )


@dataclass
class Add(BinaryOperatorType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Div(BinaryOperatorType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Mul(BinaryOperatorType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class Sub(BinaryOperatorType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"


@dataclass
class FunctionType(ExpressionType):
    literal: list[Literal] = field(
        default_factory=list,
        metadata={
            "name": "Literal",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    function: list["Function"] = field(
        default_factory=list,
        metadata={
            "name": "Function",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    property_name: list[PropertyName] = field(
        default_factory=list,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    div: list[Div] = field(
        default_factory=list,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    mul: list[Mul] = field(
        default_factory=list,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    sub: list[Sub] = field(
        default_factory=list,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    add: list[Add] = field(
        default_factory=list,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )


@dataclass
class Function(FunctionType):
    class Meta:
        namespace = "http://www.opengis.net/ogc"
