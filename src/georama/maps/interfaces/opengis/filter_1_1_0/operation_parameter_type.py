from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.operation_parameter_base_type import (
    OperationParameterBaseType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.parameter_id import ParameterId
from georama.maps.interfaces.opengis.filter_1_1_0.remarks import Remarks

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterType(OperationParameterBaseType):
    """The definition of a parameter used by an operation method.

    Most parameter values are numeric, but other types of parameter
    values are possible. This complexType is expected to be used or
    extended for all operation methods, without defining operation-
    method-specialized element names.

    :ivar parameter_id: Set of alternative identifications of this
        operation parameter. The first parameterID, if any, is normally
        the primary identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this operation
        parameter, including source information.
    """

    parameter_id: list[ParameterId] = field(
        default_factory=list,
        metadata={
            "name": "parameterID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
