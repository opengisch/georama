from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.operation_parameter_property_type import (
    OperationParameterPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationParameter2(OperationParameterPropertyType):
    """
    Gml:operationParameter is an association role to the operation parameter of
    which this is a value.
    """

    class Meta:
        name = "operationParameter"
        namespace = "http://www.opengis.net/gml/3.2"
