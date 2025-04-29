from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.operation_method_property_type import (
    OperationMethodPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Method(OperationMethodPropertyType):
    """
    Gml:method is an association role to the operation method used by a coordinate
    operation.
    """

    class Meta:
        name = "method"
        namespace = "http://www.opengis.net/gml/3.2"
