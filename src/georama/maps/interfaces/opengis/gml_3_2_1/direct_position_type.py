from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectPositionType:
    """Direct position instances hold the coordinates for a position within some
    coordinate reference system (CRS).

    Since direct positions, as data types, will often be included in
    larger objects (such as geometry elements) that have references to
    CRS, the srsName attribute will in general be missing, if this
    particular direct position is included in a larger element with such
    a reference to a CRS. In this case, the CRS is implicitly assumed to
    take on the value of the containing object's CRS. if no srsName
    attribute is given, the CRS shall be specified as part of the larger
    context this geometry element is part of, typically a geometric
    object like a point, curve, etc.
    """

    srs_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "srsName",
            "type": "Attribute",
        },
    )
    srs_dimension: Optional[int] = field(
        default=None,
        metadata={
            "name": "srsDimension",
            "type": "Attribute",
        },
    )
    axis_labels: Optional[str] = field(
        default=None,
        metadata={
            "name": "axisLabels",
            "type": "Attribute",
        },
    )
    uom_labels: Optional[str] = field(
        default=None,
        metadata={
            "name": "uomLabels",
            "type": "Attribute",
        },
    )
