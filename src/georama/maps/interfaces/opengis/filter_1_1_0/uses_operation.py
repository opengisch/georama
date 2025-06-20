from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.operation_ref_type import (
    OperationRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesOperation(OperationRefType):
    """
    Association to the operation applied to the specified ordinates.
    """

    class Meta:
        name = "usesOperation"
        namespace = "http://www.opengis.net/gml"
