from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Seconds:
    class Meta:
        name = "seconds"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[Decimal] = field(
        default=None,
        metadata={
            "required": True,
            "min_inclusive": Decimal("0.00"),
            "max_exclusive": Decimal("60.00"),
        },
    )
