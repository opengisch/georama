from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.pass_through_operation_type import (
    PassThroughOperationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PassThroughOperation(PassThroughOperationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
