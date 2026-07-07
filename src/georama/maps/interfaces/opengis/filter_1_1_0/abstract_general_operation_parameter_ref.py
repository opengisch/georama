from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_operation_parameter_ref_type import (
    AbstractGeneralOperationParameterRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameterRef(AbstractGeneralOperationParameterRefType):
    class Meta:
        name = "abstractGeneralOperationParameterRef"
        namespace = "http://www.opengis.net/gml"
