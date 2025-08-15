from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MeasureType:
    """Number with a scale.

    The value of uom (Units Of Measure) attribute is a reference to a
    Reference System for the amount, either a ratio or position scale.
    """

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
