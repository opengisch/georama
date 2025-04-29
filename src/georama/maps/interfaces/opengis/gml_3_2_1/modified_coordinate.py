from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ModifiedCoordinate:
    """
    Gml:modifiedCoordinate is a positive integer defining a position in a
    coordinate tuple.
    """

    class Meta:
        name = "modifiedCoordinate"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
