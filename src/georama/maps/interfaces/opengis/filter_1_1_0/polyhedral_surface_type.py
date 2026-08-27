from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.polygon_patches import PolygonPatches
from georama.maps.interfaces.opengis.filter_1_1_0.surface_type import SurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolyhedralSurfaceType(SurfaceType):
    """A polyhedral surface is a surface composed of polygon surfaces connected
    along their common boundary curves.

    This differs from the surface type only in the restriction on the
    types of surface patches acceptable.

    :ivar triangle_patches_or_patches:
    :ivar polygon_patches: This property encapsulates the patches of the
        polyhedral surface.
    """

    triangle_patches_or_patches: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    polygon_patches: PolygonPatches | None = field(
        default=None,
        metadata={
            "name": "polygonPatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
