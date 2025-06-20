from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.single_operation_ref_type import (
    SingleOperationRefType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesSingleOperation(SingleOperationRefType):
    """
    Association to a single operation.
    """

    class Meta:
        name = "usesSingleOperation"
        namespace = "http://www.opengis.net/gml"
