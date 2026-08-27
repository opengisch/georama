from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_surface_type import (
    AbstractSurfaceType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.patches import Patches
from georama.maps.interfaces.opengis.filter_1_1_0.polygon_patches import PolygonPatches
from georama.maps.interfaces.opengis.filter_1_1_0.triangle_patches import (
    TrianglePatches,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceType(AbstractSurfaceType):
    """A Surface is a 2-dimensional primitive and is composed of one or more
    surface patches.

    The surface patches are connected to one another. The orientation of
    the surface is positive ("up"). The orientation of a surface chooses
    an "up" direction through the choice of the upward normal, which, if
    the surface is not a cycle, is the side of the surface from which
    the exterior boundary appears counterclockwise. Reversal of the
    surface orientation reverses the curve orientation of each boundary
    component, and interchanges the conceptual "up" and "down" direction
    of the surface. If the surface is the boundary of a solid, the "up"
    direction is usually outward. For closed surfaces, which have no
    boundary, the up direction is that of the surface patches, which
    must be consistent with one another. Its included surface patches
    describe the interior structure of the Surface.
    """

    triangle_patches_or_polygon_patches_or_patches: (
        TrianglePatches | PolygonPatches | Patches | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "trianglePatches",
                    "type": TrianglePatches,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "polygonPatches",
                    "type": PolygonPatches,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "patches",
                    "type": Patches,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
