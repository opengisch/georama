from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.arc_string_type import ArcStringType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcType1(ArcStringType):
    """
    An Arc is an arc string with only one arc unit, i.e. three control points.

    :ivar num_arc: An arc is an arc string consiting of a single arc,
        the attribute is fixed to "1".
    """

    class Meta:
        name = "ArcType"

    num_arc: int = field(
        init=False,
        default=1,
        metadata={
            "name": "numArc",
            "type": "Attribute",
        },
    )
