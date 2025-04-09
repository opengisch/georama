from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_surface_property_type import (
    MultiSurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceProperty(MultiSurfacePropertyType):
    """This property element either references a surface aggregate via the XLink-
    attributes or contains the "multi surface" element.

    multiSurfaceProperty is the predefined property, which may be used
    by GML Application Schemas whenever a GML feature has a property
    with a value that is substitutable for MultiSurface.
    """

    class Meta:
        name = "multiSurfaceProperty"
        namespace = "http://www.opengis.net/gml"
