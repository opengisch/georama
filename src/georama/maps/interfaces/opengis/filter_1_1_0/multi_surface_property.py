from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.multi_surface_property_type import (
    MultiSurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceProperty(MultiSurfacePropertyType):
    """This property element either references a surface aggregate via the XLink-
    attributes or contains the "multi surface" element.

    multiSurfaceProperty is the predefined property which can be used by
    GML Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for MultiSurface.
    """

    class Meta:
        name = "multiSurfaceProperty"
        namespace = "http://www.opengis.net/gml"
