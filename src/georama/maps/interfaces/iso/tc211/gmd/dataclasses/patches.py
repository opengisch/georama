from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_patch_array_property_type import (
    SurfacePatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Patches(SurfacePatchArrayPropertyType):
    """The patches property element contains the sequence of surface patches.

    The order of the elements is significant and shall be preserved when
    processing the array.
    """

    class Meta:
        name = "patches"
        namespace = "http://www.opengis.net/gml"
