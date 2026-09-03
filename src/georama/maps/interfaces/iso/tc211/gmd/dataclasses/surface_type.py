from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_surface_type import (
    AbstractSurfaceType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.patches import Patches
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polygon_patches import (
    PolygonPatches,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.triangle_patches import (
    TrianglePatches,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceType(AbstractSurfaceType):
    triangle_patches: TrianglePatches | None = field(
        default=None,
        metadata={
            "name": "trianglePatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon_patches: PolygonPatches | None = field(
        default=None,
        metadata={
            "name": "polygonPatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    patches: Patches | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
