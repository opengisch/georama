from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polygon_patches import (
    PolygonPatches,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_type import SurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolyhedralSurfaceType(SurfaceType):
    triangle_patches: Any = field(
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
    polygon_patches: PolygonPatches | None = field(
        default=None,
        metadata={
            "name": "polygonPatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
