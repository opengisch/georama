from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class IntegerValue:
    """Gml:integerValue is a positive integer value of an operation parameter,
    usually used for a count.

    An integer value does not have an associated unit of measure.
    """

    class Meta:
        name = "integerValue"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
