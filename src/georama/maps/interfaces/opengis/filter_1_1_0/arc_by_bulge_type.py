from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.arc_string_by_bulge_type import (
    ArcStringByBulgeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcByBulgeType(ArcStringByBulgeType):
    """
    An ArcByBulge is an arc string with only one arc unit, i.e. two control points
    and one bulge.

    :ivar num_arc: An arc is an arc string consiting of a single arc,
        the attribute is fixed to "1".
    """

    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        },
    )
