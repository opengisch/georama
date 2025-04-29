from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_surface_type import (
    AbstractSurfaceType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.patches import Patches
from georama.maps.interfaces.opengis.gml_3_2_1.polygon_patches import PolygonPatches
from georama.maps.interfaces.opengis.gml_3_2_1.triangle_patches import TrianglePatches

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceType(AbstractSurfaceType):
    triangle_patches: Optional[TrianglePatches] = field(
        default=None,
        metadata={
            "name": "trianglePatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polygon_patches: Optional[PolygonPatches] = field(
        default=None,
        metadata={
            "name": "polygonPatches",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    patches: Optional[Patches] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
