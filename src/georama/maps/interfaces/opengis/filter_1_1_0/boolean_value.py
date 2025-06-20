from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BooleanValue:
    """Boolean value of an operation parameter.

    A Boolean value does not have an associated unit of measure.
    """

    class Meta:
        name = "booleanValue"
        namespace = "http://www.opengis.net/gml"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
