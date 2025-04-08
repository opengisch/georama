from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.single_operation_property_type import (
    SingleOperationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SingleOperationRef(SingleOperationPropertyType):
    class Meta:
        name = "singleOperationRef"
        namespace = "http://www.opengis.net/gml"
