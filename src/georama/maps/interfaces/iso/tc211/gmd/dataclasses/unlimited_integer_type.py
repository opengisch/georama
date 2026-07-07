from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class UnlimitedIntegerType:
    class Meta:
        name = "UnlimitedInteger_Type"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    is_infinite: Optional[bool] = field(
        default=None,
        metadata={
            "name": "isInfinite",
            "type": "Attribute",
        },
    )
