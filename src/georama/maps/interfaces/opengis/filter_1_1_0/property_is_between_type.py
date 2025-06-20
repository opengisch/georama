from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.binary_operator_type import (
    Add,
    Div,
    Function,
    Mul,
    Sub,
)
from georama.maps.interfaces.opengis.filter_1_1_0.comparison_ops_type import (
    ComparisonOpsType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.literal import Literal
from georama.maps.interfaces.opengis.filter_1_1_0.lower_boundary_type import (
    LowerBoundaryType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_name import PropertyName
from georama.maps.interfaces.opengis.filter_1_1_0.upper_boundary_type import (
    UpperBoundaryType,
)

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class PropertyIsBetweenType(ComparisonOpsType):
    literal: Optional[Literal] = field(
        default=None,
        metadata={
            "name": "Literal",
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
    property_name: Optional[PropertyName] = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    div: Optional[Div] = field(
        default=None,
        metadata={
            "name": "Div",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    mul: Optional[Mul] = field(
        default=None,
        metadata={
            "name": "Mul",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    sub: Optional[Sub] = field(
        default=None,
        metadata={
            "name": "Sub",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    add: Optional[Add] = field(
        default=None,
        metadata={
            "name": "Add",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    lower_boundary: Optional[LowerBoundaryType] = field(
        default=None,
        metadata={
            "name": "LowerBoundary",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        },
    )
    upper_boundary: Optional[UpperBoundaryType] = field(
        default=None,
        metadata={
            "name": "UpperBoundary",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
            "required": True,
        },
    )
