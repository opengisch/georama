from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.surface_patch_array_property_type import (
    SurfacePatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Patches(SurfacePatchArrayPropertyType):
    """The patches property element contains the sequence of surface patches.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "patches"
        namespace = "http://www.opengis.net/gml/3.2"
