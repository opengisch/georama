from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_operation_parameter_ref_type import (
    AbstractGeneralOperationParameterRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesParameter(AbstractGeneralOperationParameterRefType):
    """
    Association to an operation parameter or parameter group used by this operation
    method.
    """

    class Meta:
        name = "usesParameter"
        namespace = "http://www.opengis.net/gml"
