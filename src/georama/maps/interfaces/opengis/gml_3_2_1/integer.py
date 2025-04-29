from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Integer:
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
