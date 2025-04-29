from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Boolean2:
    class Meta:
        name = "Boolean"
        namespace = "http://www.isotc211.org/2005/gco"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
