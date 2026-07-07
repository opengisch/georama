from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.concatenated_operation_property_type import (
    ConcatenatedOperationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConcatenatedOperationRef(ConcatenatedOperationPropertyType):
    class Meta:
        name = "concatenatedOperationRef"
        namespace = "http://www.opengis.net/gml"
