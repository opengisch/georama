from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Boolean:
    """A value from two-valued logic, using the XML Schema boolean type.

    An instance may take the values {true, false, 1, 0}.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: Optional[bool] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
