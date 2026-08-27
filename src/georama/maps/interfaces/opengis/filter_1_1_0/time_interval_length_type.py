from dataclasses import dataclass, field
from decimal import Decimal

from georama.maps.interfaces.opengis.filter_1_1_0.time_unit_type_value import (
    TimeUnitTypeValue,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimeIntervalLengthType:
    """This type extends the built-in xsd:decimal simple type to allow floating-
    point values for temporal length.

    According to  the ISO 11404 model you have to use positiveInteger
    together with appropriate values for radix and factor. The
    resolution of the time interval is to one radix ^(-factor) of the
    specified time unit (e.g. unit="second", radix="10", factor="3"
    specifies a resolution of milliseconds). It is a subtype of
    TimeDurationType.
    """

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
