from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_array_property_type import (
    SurfaceArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SurfaceArrayProperty(SurfaceArrayPropertyType):
    """This property element contains a list of surface elements.

    surfaceArrayProperty is the predefined property which may be used by
    GML Application Schemas whenever a GML feature has a property with a
    value that is substitutable for a list of AbstractSurfaces.
    """

    class Meta:
        name = "surfaceArrayProperty"
        namespace = "http://www.opengis.net/gml"
