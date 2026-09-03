from dataclasses import dataclass, field
from decimal import Decimal

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordType:
    """Represents a coordinate tuple in one, two, or three dimensions.

    Deprecated with GML 3.0 and replaced by DirectPositionType.
    """

    x: Decimal | None = field(
        default=None,
        metadata={
            "name": "X",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    y: Decimal | None = field(
        default=None,
        metadata={
            "name": "Y",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    z: Decimal | None = field(
        default=None,
        metadata={
            "name": "Z",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
