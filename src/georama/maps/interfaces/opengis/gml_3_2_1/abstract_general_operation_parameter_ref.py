from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_general_operation_parameter_property_type import (
    AbstractGeneralOperationParameterPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralOperationParameterRef(
    AbstractGeneralOperationParameterPropertyType
):
    class Meta:
        name = "abstractGeneralOperationParameterRef"
        namespace = "http://www.opengis.net/gml/3.2"
