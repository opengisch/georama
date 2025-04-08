from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.pass_through_operation_property_type import (
    PassThroughOperationPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PassThroughOperationRef(PassThroughOperationPropertyType):
    class Meta:
        name = "passThroughOperationRef"
        namespace = "http://www.opengis.net/gml"
