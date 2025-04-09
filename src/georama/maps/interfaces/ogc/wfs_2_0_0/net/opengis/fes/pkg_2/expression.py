from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class Expression:
    class Meta:
        name = "expression"
        namespace = "http://www.opengis.net/fes/2.0"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
