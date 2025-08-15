from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FunctionNameType:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    n_args: Optional[str] = field(
        default=None,
        metadata={
            "name": "nArgs",
            "type": "Attribute",
            "required": True,
        },
    )
