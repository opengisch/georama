from dataclasses import dataclass, field
from typing import Any, Optional

from georama.maps.interfaces.opengis.filter_1_1_0.surface_type import SurfaceType
from georama.maps.interfaces.opengis.filter_1_1_0.triangle_patches import (
    TrianglePatches,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TriangulatedSurfaceType(SurfaceType):
    """A triangulated surface is a polyhedral surface that is composed only of
    triangles.

    There is no restriction on how the triangulation is derived.

    :ivar polygon_patches:
    :ivar patches: This element encapsulates the patches of the surface.
    :ivar triangle_patches: This property encapsulates the patches of
        the triangulated surface.
    """

    polygon_patches: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    patches: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    triangle_patches: Optional[TrianglePatches] = field(
        default=None,
        metadata={
            "name": "trianglePatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
