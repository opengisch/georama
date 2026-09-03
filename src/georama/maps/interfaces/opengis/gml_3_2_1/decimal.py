from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class DecimalType:
    class Meta:
        name = "Decimal"
        namespace = "http://www.isotc211.org/2005/gco"

    value: Decimal | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
