from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.affine_placement_type import (
    AffinePlacementType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AffinePlacement(AffinePlacementType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
