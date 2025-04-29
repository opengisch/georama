from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class MinimumOccurs:
    """Gml:minimumOccurs is the minimum number of times that values for this
    parameter group or parameter are required.

    If this attribute is omitted, the minimum number shall be one.
    """

    class Meta:
        name = "minimumOccurs"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
