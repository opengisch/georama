from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class DecimalType:
    class Meta:
        name = "Decimal"
        namespace = "http://www.isotc211.org/2005/gco"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
