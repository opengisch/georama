from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectPositionListType:
    """PosList instances (and other instances with the content model specified by
    DirectPositionListType) hold the coordinates for a sequence of direct positions
    within the same coordinate reference system (CRS).

    if no srsName attribute is given, the CRS shall be specified as part
    of the larger context this geometry element is part of, typically a
    geometric object like a point, curve, etc. The optional attribute
    count specifies the number of direct positions in the list. If the
    attribute count is present then the attribute srsDimension shall be
    present, too. The number of entries in the list is equal to the
    product of the dimensionality of the coordinate reference system
    (i.e. it is a derived value of the coordinate reference system
    definition) and the number of direct positions.
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
    count: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
