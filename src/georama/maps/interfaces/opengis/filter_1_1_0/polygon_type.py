from dataclasses import dataclass, field
from typing import Optional

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

    outer_boundary_is: Optional[OuterBoundaryIs] = field(
        default=None,
        metadata={
            "name": "outerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    exterior: Optional[Exterior] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    inner_boundary_is: list[InnerBoundaryIs] = field(
        default_factory=list,
        metadata={
            "name": "innerBoundaryIs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    interior: list[Interior] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
