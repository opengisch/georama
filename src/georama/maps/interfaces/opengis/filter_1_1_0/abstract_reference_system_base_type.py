from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType
from georama.maps.interfaces.opengis.filter_1_1_0.srs_name import SrsName

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractReferenceSystemBaseType(DefinitionType):
    """
    Basic encoding for reference system objects, simplifying and restricting the
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
    srs_name: list[SrsName] = field(
        default_factory=list,
        metadata={
            "name": "srsName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
