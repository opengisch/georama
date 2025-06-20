from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MinimumOccurs:
    """The minimum number of times that values for this parameter group or
    parameter are required.

    If this attribute is omitted, the minimum number is one.
    """

    class Meta:
        name = "minimumOccurs"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
