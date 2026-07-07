from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.concatenated_operation_type import (
    ConcatenatedOperationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConcatenatedOperation(ConcatenatedOperationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
