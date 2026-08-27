from dataclasses import dataclass, field
from typing import ForwardRef, Union

from georama.maps.interfaces.opengis.filter_1_1_0.expression_type import ExpressionType
from georama.maps.interfaces.opengis.filter_1_1_0.literal import Literal
from georama.maps.interfaces.opengis.filter_1_1_0.property_name import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class BinaryOperatorType(ExpressionType):
    choice: list[
        Union[Literal, "Function", PropertyName, "Div", "Mul", "Sub", "Add"]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Literal",
                    "type": Literal,
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "Function",
                    "type": ForwardRef("Function"),
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "PropertyName",
                    "type": PropertyName,
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "Div",
                    "type": ForwardRef("Div"),
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "Mul",
                    "type": ForwardRef("Mul"),
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "Sub",
                    "type": ForwardRef("Sub"),
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
                {
                    "name": "Add",
                    "type": ForwardRef("Add"),
                    "namespace": "http://www.opengis.net/ogc",
                    "max_occurs": 2,
                },
            ),
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
    choice: list[Union[Literal, "Function", PropertyName, Div, Mul, Sub, Add]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Literal",
                    "type": Literal,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Function",
                    "type": ForwardRef("Function"),
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "PropertyName",
                    "type": PropertyName,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Div",
                    "type": Div,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Mul",
                    "type": Mul,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Sub",
                    "type": Sub,
                    "namespace": "http://www.opengis.net/ogc",
                },
                {
                    "name": "Add",
                    "type": Add,
                    "namespace": "http://www.opengis.net/ogc",
                },
            ),
        },
    )
    name: str | None = field(
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
