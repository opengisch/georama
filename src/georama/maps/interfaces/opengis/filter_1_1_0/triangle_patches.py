from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.triangle_patch_array_property_type import (
    TrianglePatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TrianglePatches(TrianglePatchArrayPropertyType):
    """This property element contains a list of triangle patches.

    The order of the patches is significant and shall be preserved when
    processing the list.
    """

    class Meta:
        name = "trianglePatches"
        namespace = "http://www.opengis.net/gml"
