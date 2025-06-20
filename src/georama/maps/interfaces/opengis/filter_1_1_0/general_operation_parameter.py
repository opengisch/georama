from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_operation_parameter_type import (
    AbstractGeneralOperationParameterType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeneralOperationParameter(AbstractGeneralOperationParameterType):
    class Meta:
        name = "_GeneralOperationParameter"
        namespace = "http://www.opengis.net/gml"
