from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MeasureListType:
    """
    Gml:MeasureListType provides for a list of quantities.
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
            "pattern": r"[^: \n\r\t]+",
        },
    )
