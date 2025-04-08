from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.arc_type import ArcType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Arc(ArcType):
    """An Arc is an arc string with only one arc unit, i.e. three control points
    including the start and end point.

    As arc is an arc string consisting of a single arc, the attribute
    “numArc” is fixed to "1".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
