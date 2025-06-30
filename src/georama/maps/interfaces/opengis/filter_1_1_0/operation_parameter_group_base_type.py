from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_operation_parameter_type import (
    AbstractGeneralOperationParameterType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.group_name import GroupName

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterGroupBaseType(AbstractGeneralOperationParameterType):
    """
    Basic encoding for operation parameter group objects, simplifying and
    restricting the DefinitionType as needed.
    """

    description: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    group_name: list[GroupName] = field(
        default_factory=list,
        metadata={
            "name": "groupName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
