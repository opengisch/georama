from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.arc_by_bulge_type import ArcByBulgeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ArcByBulge(ArcByBulgeType):
    """An ArcByBulge is an arc string with only one arc unit, i.e. two control
    points, one bulge and one normal vector.

    As arc is an arc string consisting of a single arc, the attribute
    "numArc" is fixed to "1".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
