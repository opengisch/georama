from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.surface_property_type import (
    SurfacePropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SurfaceProperty(SurfacePropertyType):
    """This property element either references a surface via the XLink-attributes
    or contains the surface element.

    surfaceProperty is the predefined property which may be used by GML
    Application Schemas whenever a GML feature has a property with a
    value that is substitutable for AbstractSurface.
    """

    class Meta:
        name = "surfaceProperty"
        namespace = "http://www.opengis.net/gml/3.2"
