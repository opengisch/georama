from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordType:
    """Represents a coordinate tuple in one, two, or three dimensions.

    Deprecated with GML 3.0 and replaced by DirectPositionType.
    """

    x: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    y: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    z: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
