from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.arc_by_bulge_type import (
    ArcByBulgeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArcByBulge(ArcByBulgeType):
    """An ArcByBulge is an arc string with only one arc unit, i.e. two control
    points, one bulge and one normal vector.

    As arc is an arc string consisting of a single arc, the attribute
    “numArc” is fixed to "1".
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
