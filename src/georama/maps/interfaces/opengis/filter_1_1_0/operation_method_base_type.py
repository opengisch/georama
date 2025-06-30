from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType
from georama.maps.interfaces.opengis.filter_1_1_0.method_name import MethodName

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationMethodBaseType(DefinitionType):
    """
    Basic encoding for operation method objects, simplifying and restricting the
    DefinitionType as needed.
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
    method_name: list[MethodName] = field(
        default_factory=list,
        metadata={
            "name": "methodName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
