from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.surface_patch_array_property_type import (
    SurfacePatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class PolygonPatches(SurfacePatchArrayPropertyType):
    class Meta:
        name = "polygonPatches"
        namespace = "http://www.opengis.net/gml/3.2"
