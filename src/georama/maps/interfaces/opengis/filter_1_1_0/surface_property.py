from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.surface_property_type import (
    SurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceProperty(SurfacePropertyType):
    """This property element either references a surface via the XLink-attributes
    or contains the surface element.

    surfaceProperty is the predefined property which can be used by GML
    Application Schemas whenever a GML Feature has a property with a
    value that is substitutable for _Surface.
    """

    class Meta:
        name = "surfaceProperty"
        namespace = "http://www.opengis.net/gml"
