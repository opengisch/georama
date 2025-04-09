from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/fes/2.0"


@dataclass
class AbstractQueryExpressionType:
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
