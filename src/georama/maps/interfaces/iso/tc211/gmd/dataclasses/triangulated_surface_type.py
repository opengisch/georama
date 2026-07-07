from dataclasses import dataclass, field
from typing import Any, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_type import SurfaceType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.triangle_patches import (
    TrianglePatches,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TriangulatedSurfaceType(SurfaceType):
    polygon_patches: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    patches: Any = field(
        init=False,
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
