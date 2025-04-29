from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.concatenated_operation_property_type import (
    ConcatenatedOperationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ConcatenatedOperationRef(ConcatenatedOperationPropertyType):
    class Meta:
        name = "concatenatedOperationRef"
        namespace = "http://www.opengis.net/gml/3.2"
