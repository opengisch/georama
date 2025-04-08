from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polygon_patch_array_property_type import (
    PolygonPatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatches(PolygonPatchArrayPropertyType):
    class Meta:
        name = "polygonPatches"
        namespace = "http://www.opengis.net/gml"
