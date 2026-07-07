from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.surface_patch_array_property_type import (
    SurfacePatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Patches(SurfacePatchArrayPropertyType):
    """This property element contains a list of surface patches.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "patches"
        namespace = "http://www.opengis.net/gml"
