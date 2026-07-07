from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_datum_type import (
    AbstractDatumType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_datum_type import (
    VerticalDatumType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalDatumType1(AbstractDatumType):
    """A textual description and/or a set of parameters identifying a particular
    reference level surface used as a zero-height surface, including its position
    with respect to the Earth for any of the height types recognized by this
    standard.

    There are several types of Vertical Datums, and each may place
    constraints on the Coordinate Axis with which it is combined to
    create a Vertical CRS.
    """

    class Meta:
        name = "VerticalDatumType"

    vertical_datum_type: Optional[VerticalDatumType] = field(
        default=None,
        metadata={
            "name": "verticalDatumType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
