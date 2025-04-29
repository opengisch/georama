from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.single_operation_property_type import (
    SingleOperationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SingleOperationRef(SingleOperationPropertyType):
    class Meta:
        name = "singleOperationRef"
        namespace = "http://www.opengis.net/gml/3.2"
