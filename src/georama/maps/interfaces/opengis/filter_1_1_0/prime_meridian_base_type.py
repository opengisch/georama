from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType
from georama.maps.interfaces.opengis.filter_1_1_0.meridian_name import MeridianName

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PrimeMeridianBaseType(DefinitionType):
    """
    Basic encoding for prime meridian objects, simplifying and restricting the
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
    meridian_name: list[MeridianName] = field(
        default_factory=list,
        metadata={
            "name": "meridianName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
