from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.pass_through_operation_property_type import (
    PassThroughOperationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PassThroughOperationRef(PassThroughOperationPropertyType):
    class Meta:
        name = "passThroughOperationRef"
        namespace = "http://www.opengis.net/gml/3.2"
