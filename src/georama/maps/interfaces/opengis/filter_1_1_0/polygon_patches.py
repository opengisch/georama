from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.polygon_patch_array_property_type import (
    PolygonPatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatches(PolygonPatchArrayPropertyType):
    """This property element contains a list of polygon patches.

    The order of the patches is significant and shall be preserved when
    processing the list.
    """

    class Meta:
        name = "polygonPatches"
        namespace = "http://www.opengis.net/gml"
