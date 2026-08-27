from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_general_parameter_value_property_type import (
    IncludesValue,
    ParameterValue2,
    UsesValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.abstract_general_transformation_type import (
    AbstractGeneralTransformationType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.method import Method
from georama.maps.interfaces.opengis.gml_3_2_1.uses_method import UsesMethod

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TransformationType(AbstractGeneralTransformationType):
    uses_method: UsesMethod | None = field(
        default=None,
        metadata={
            "name": "usesMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    method: Method | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    includes_value: list[IncludesValue] = field(
        default_factory=list,
        metadata={
            "name": "includesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_value: list[UsesValue] = field(
        default_factory=list,
        metadata={
            "name": "usesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    parameter_value: list[ParameterValue2] = field(
        default_factory=list,
        metadata={
            "name": "parameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
