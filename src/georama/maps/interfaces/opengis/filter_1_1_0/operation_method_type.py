from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.method_formula import MethodFormula
from georama.maps.interfaces.opengis.filter_1_1_0.method_id import MethodId
from georama.maps.interfaces.opengis.filter_1_1_0.operation_method_base_type import (
    OperationMethodBaseType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.remarks import Remarks
from georama.maps.interfaces.opengis.filter_1_1_0.source_dimensions import (
    SourceDimensions,
)
from georama.maps.interfaces.opengis.filter_1_1_0.target_dimensions import (
    TargetDimensions,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_parameter import UsesParameter

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationMethodType(OperationMethodBaseType):
    """Definition of an algorithm used to perform a coordinate operation.

    Most operation methods use a number of operation parameters,
    although some coordinate conversions use none. Each coordinate
    operation using the method assigns values to these parameters.

    :ivar method_id: Set of alternative identifications of this
        operation method. The first methodID, if any, is normally the
        primary identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this operation
        method, including source information.
    :ivar method_formula:
    :ivar source_dimensions:
    :ivar target_dimensions:
    :ivar uses_parameter: Unordered list of associations to the set of
        operation parameters and parameter groups used by this operation
        method.
    """

    method_id: list[MethodId] = field(
        default_factory=list,
        metadata={
            "name": "methodID",
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
    method_formula: Optional[MethodFormula] = field(
        default=None,
        metadata={
            "name": "methodFormula",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    source_dimensions: Optional[SourceDimensions] = field(
        default=None,
        metadata={
            "name": "sourceDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    target_dimensions: Optional[TargetDimensions] = field(
        default=None,
        metadata={
            "name": "targetDimensions",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    uses_parameter: list[UsesParameter] = field(
        default_factory=list,
        metadata={
            "name": "usesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
