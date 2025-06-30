from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType
from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoid_name import EllipsoidName

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EllipsoidBaseType(DefinitionType):
    """
    Basic encoding for ellipsoid objects, simplifying and restricting the
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
    ellipsoid_name: list[EllipsoidName] = field(
        default_factory=list,
        metadata={
            "name": "ellipsoidName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
