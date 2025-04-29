from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.affine_placement_type import (
    AffinePlacementType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AffinePlacement(AffinePlacementType):
    """
    Location, refDirection, inDimension and outDimension have the same meaning as
    specified in ISO 19107:2003, 6.4.21.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
