from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.domain_set_type import DomainSetType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolidDomainType(DomainSetType):
    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
