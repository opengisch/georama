from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BooleanValue:
    """Gml:booleanValue is a boolean value of an operation parameter.

    A Boolean value does not have an associated unit of measure.
    """

    class Meta:
        name = "booleanValue"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
