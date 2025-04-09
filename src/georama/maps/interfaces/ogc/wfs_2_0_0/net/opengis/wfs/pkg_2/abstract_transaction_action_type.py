from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class AbstractTransactionActionType:
    handle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
