from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.triangle_patch_array_property_type import (
    TrianglePatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TrianglePatches(TrianglePatchArrayPropertyType):
    class Meta:
        name = "trianglePatches"
        namespace = "http://www.opengis.net/gml"
