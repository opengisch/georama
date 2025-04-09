from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.affine_placement_type import (
    AffinePlacementType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AffinePlacement(AffinePlacementType):
    """
    Location, refDirection, inDimension and outDimension have the same meaning as
    specified in ISO 19107:2003, 6.4.21.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
