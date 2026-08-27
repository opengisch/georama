from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_parameter_value_property_type import (
    IncludesValue,
    ParameterValue2,
    UsesValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_transformation_type import (
    AbstractGeneralTransformationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.method import Method
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.uses_method import UsesMethod

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TransformationType(AbstractGeneralTransformationType):
    uses_method: UsesMethod | None = field(
        default=None,
        metadata={
            "name": "usesMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    method: Method | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    includes_value: list[IncludesValue] = field(
        default_factory=list,
        metadata={
            "name": "includesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    uses_value: list[UsesValue] = field(
        default_factory=list,
        metadata={
            "name": "usesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    parameter_value: list[ParameterValue2] = field(
        default_factory=list,
        metadata={
            "name": "parameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
