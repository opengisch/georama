from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_surface_type import (
    AbstractSurfaceType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.exterior import Exterior
from georama.maps.interfaces.opengis.filter_1_1_0.inner_boundary_is import (
    InnerBoundaryIs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.interior import Interior
from georama.maps.interfaces.opengis.filter_1_1_0.outer_boundary_is import (
    OuterBoundaryIs,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonType(AbstractSurfaceType):
    """A Polygon is a special surface that is defined by a single surface patch.

    The boundary of this patch is coplanar and the polygon uses planar
    interpolation in its interior. It is backwards compatible with the
    Polygon of GML 2, GM_Polygon of ISO 19107 is implemented by
    PolygonPatch.
    """

    outer_boundary_is_or_exterior: Optional[Union[OuterBoundaryIs, Exterior]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "outerBoundaryIs",
                    "type": OuterBoundaryIs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "exterior",
                    "type": Exterior,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    inner_boundary_is_or_interior: list[Union[InnerBoundaryIs, Interior]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "innerBoundaryIs",
                    "type": InnerBoundaryIs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "interior",
                    "type": Interior,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
