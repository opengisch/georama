from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class OtherCrs:
    class Meta:
        global_type = False

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
