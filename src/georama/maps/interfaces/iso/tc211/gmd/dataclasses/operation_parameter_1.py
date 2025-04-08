from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_parameter_type import (
    OperationParameterType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameter1(OperationParameterType):
    """Gml:OperationParameter is the definition of a parameter used by an operation
    method.

    Most parameter values are numeric, but other types of parameter
    values are possible. This complex type is expected to be used or
    extended for all operation methods, without defining operation-
    method-specialized element names.
    """

    class Meta:
        name = "OperationParameter"
        namespace = "http://www.opengis.net/gml"
