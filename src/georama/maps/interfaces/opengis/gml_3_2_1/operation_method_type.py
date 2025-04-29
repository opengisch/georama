from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_general_operation_parameter_property_type import (
    GeneralOperationParameter,
    IncludesParameter,
    Parameter,
    UsesParameter,
)
from georama.maps.interfaces.opengis.gml_3_2_1.formula import Formula
from georama.maps.interfaces.opengis.gml_3_2_1.formula_citation import FormulaCitation
from georama.maps.interfaces.opengis.gml_3_2_1.identified_object_type import (
    IdentifiedObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.method_formula import MethodFormula
from georama.maps.interfaces.opengis.gml_3_2_1.source_dimensions import SourceDimensions
from georama.maps.interfaces.opengis.gml_3_2_1.target_dimensions import TargetDimensions

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationMethodType(IdentifiedObjectType):
    formula_citation: Optional[FormulaCitation] = field(
        default=None,
        metadata={
            "name": "formulaCitation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    method_formula: Optional[MethodFormula] = field(
        default=None,
        metadata={
            "name": "methodFormula",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    formula: Optional[Formula] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    source_dimensions: Optional[SourceDimensions] = field(
        default=None,
        metadata={
            "name": "sourceDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    target_dimensions: Optional[TargetDimensions] = field(
        default=None,
        metadata={
            "name": "targetDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_parameter: list[UsesParameter] = field(
        default_factory=list,
        metadata={
            "name": "usesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    general_operation_parameter: list[GeneralOperationParameter] = field(
        default_factory=list,
        metadata={
            "name": "generalOperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    includes_parameter: list[IncludesParameter] = field(
        default_factory=list,
        metadata={
            "name": "includesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    parameter: list[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
