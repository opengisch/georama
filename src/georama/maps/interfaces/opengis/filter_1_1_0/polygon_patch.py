from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.polygon_patch_type import (
    PolygonPatchType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatch(PolygonPatchType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
