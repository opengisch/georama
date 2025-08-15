from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.arc_type_1 import ArcType1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Arc(ArcType1):
    """An Arc is an arc string with only one arc unit, i.e. three control points
    including the start and end point.

    As arc is an arc string consisting of a single arc, the attribute
    "numArc" is fixed to "1".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
