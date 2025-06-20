from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.affine_placement import (
    AffinePlacement,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ClothoidTypeRefLocation:
    """
    :ivar affine_placement: The "refLocation" is an affine mapping that
        places  the curve defined by the Fresnel Integrals into the co-
        ordinate reference system of this object.
    """

    class Meta:
        global_type = False

    affine_placement: Optional[AffinePlacement] = field(
        default=None,
        metadata={
            "name": "AffinePlacement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
