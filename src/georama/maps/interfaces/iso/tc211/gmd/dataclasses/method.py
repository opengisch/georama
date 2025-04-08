from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_method_property_type import (
    OperationMethodPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Method(OperationMethodPropertyType):
    """
    Gml:method is an association role to the operation method used by a coordinate
    operation.
    """

    class Meta:
        name = "method"
        namespace = "http://www.opengis.net/gml"
