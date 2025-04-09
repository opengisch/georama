from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_parameter_property_type import (
    OperationParameterPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterGroupRef(OperationParameterPropertyType):
    class Meta:
        name = "operationParameterGroupRef"
        namespace = "http://www.opengis.net/gml"
