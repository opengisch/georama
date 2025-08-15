from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class IntegerValue:
    """Positive integer value of an operation parameter, usually used for a count.

    An integer value does not have an associated unit of measure.
    """

    class Meta:
        name = "integerValue"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
