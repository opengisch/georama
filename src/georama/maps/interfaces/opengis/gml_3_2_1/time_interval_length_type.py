from dataclasses import dataclass, field
from decimal import Decimal

from georama.maps.interfaces.opengis.gml_3_2_1.time_unit_type_value import (
    TimeUnitTypeValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TimeIntervalLengthType:
    value: Decimal | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    unit: str | TimeUnitTypeValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"other:\w{2,}",
        },
    )
    radix: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    factor: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
