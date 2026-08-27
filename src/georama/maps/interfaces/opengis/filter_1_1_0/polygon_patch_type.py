from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_surface_patch_type import (
    AbstractSurfacePatchType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.exterior import Exterior
from georama.maps.interfaces.opengis.filter_1_1_0.inner_boundary_is import (
    InnerBoundaryIs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.interior import Interior
from georama.maps.interfaces.opengis.filter_1_1_0.outer_boundary_is import (
    OuterBoundaryIs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.surface_interpolation_type import (
    SurfaceInterpolationType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatchType(AbstractSurfacePatchType):
    """A PolygonPatch is a surface patch that is defined by a set of boundary
    curves and an underlying surface to which these curves adhere.

    The curves are coplanar and the polygon uses planar interpolation in
    its interior. Implements GM_Polygon of ISO 19107.

    :ivar outer_boundary_is_or_exterior:
    :ivar inner_boundary_is_or_interior:
    :ivar interpolation: The attribute "interpolation" specifies the
        interpolation mechanism used for this surface patch. Currently
        only planar surface patches are defined in GML 3, the attribute
        is fixed to "planar", i.e. the interpolation method shall return
        points on a single plane. The boundary of the patch shall be
        contained within that plane.
    """

    outer_boundary_is_or_exterior: OuterBoundaryIs | Exterior | None = field(
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
    inner_boundary_is_or_interior: list[InnerBoundaryIs | Interior] = field(
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
    interpolation: SurfaceInterpolationType = field(
        init=False,
        default=SurfaceInterpolationType.PLANAR,
        metadata={
            "type": "Attribute",
        },
    )
