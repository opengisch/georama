from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_parameter_property_type import (
    OperationParameterPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterRef(OperationParameterPropertyType):
    class Meta:
        name = "operationParameterRef"
        namespace = "http://www.opengis.net/gml"
