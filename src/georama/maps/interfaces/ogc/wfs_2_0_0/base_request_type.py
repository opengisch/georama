from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class BaseRequestType:
    service: str = field(
        init=False,
        default="WFS",
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"2\.0\.\d+",
        },
    )
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
