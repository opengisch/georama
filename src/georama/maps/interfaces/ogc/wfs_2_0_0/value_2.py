from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class Value2:
    class Meta:
        name = "Value"
        namespace = "http://www.opengis.net/wfs/2.0"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
