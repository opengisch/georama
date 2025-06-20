from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Count:
    """
    An integer representing a frequency of occurrence.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
