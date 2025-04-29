from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.operation_parameter_property_type import (
    OperationParameterPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ValueOfParameter(OperationParameterPropertyType):
    class Meta:
        name = "valueOfParameter"
        namespace = "http://www.opengis.net/gml/3.2"
