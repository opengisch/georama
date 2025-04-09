from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_parameter_group_property_type import (
    OperationParameterGroupPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ValuesOfGroup(OperationParameterGroupPropertyType):
    class Meta:
        name = "valuesOfGroup"
        namespace = "http://www.opengis.net/gml"
