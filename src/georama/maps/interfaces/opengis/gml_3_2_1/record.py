from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Record:
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
