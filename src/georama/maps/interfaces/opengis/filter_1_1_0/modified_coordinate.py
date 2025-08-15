from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ModifiedCoordinate:
    """
    A positive integer defining a position in a coordinate tuple.
    """

    class Meta:
        name = "modifiedCoordinate"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
