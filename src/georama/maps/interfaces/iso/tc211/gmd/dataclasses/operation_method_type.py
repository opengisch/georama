from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_operation_parameter_property_type import (
    GeneralOperationParameter,
    UsesParameter,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.formula import Formula
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.identified_object_type import (
    IdentifiedObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.method_formula import (
    MethodFormula,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.source_dimensions import (
    SourceDimensions,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.target_dimensions import (
    TargetDimensions,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationMethodType(IdentifiedObjectType):
    method_formula: MethodFormula | None = field(
        default=None,
        metadata={
            "name": "methodFormula",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    formula: Formula | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    source_dimensions: SourceDimensions | None = field(
        default=None,
        metadata={
            "name": "sourceDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    target_dimensions: TargetDimensions | None = field(
        default=None,
        metadata={
            "name": "targetDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    uses_parameter: list[UsesParameter] = field(
        default_factory=list,
        metadata={
            "name": "usesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    general_operation_parameter: list[GeneralOperationParameter] = field(
        default_factory=list,
        metadata={
            "name": "generalOperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
