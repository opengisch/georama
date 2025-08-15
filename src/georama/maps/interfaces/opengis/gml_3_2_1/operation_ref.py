from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.operation_property_type import (
    OperationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationRef(OperationPropertyType):
    class Meta:
        name = "operationRef"
        namespace = "http://www.opengis.net/gml/3.2"
