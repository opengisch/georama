from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MeasureListType:
    """List of numbers with a uniform scale.

    The value of uom (Units Of Measure) attribute is a reference to a
    Reference System for the amount, either a ratio or position scale.
    """

    value: list[float] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
