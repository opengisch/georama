from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.binary_operator_type import (
    Add,
    Div,
    Function,
    Mul,
    Sub,
)
from georama.maps.interfaces.opengis.filter_1_1_0.literal import Literal
from georama.maps.interfaces.opengis.filter_1_1_0.property_name import PropertyName

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class UpperBoundaryType:
    choice: Optional[Union[Literal, Function, PropertyName, Div, Mul, Sub, Add]] = field(
        default=None,
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
                    "type": Function,
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
