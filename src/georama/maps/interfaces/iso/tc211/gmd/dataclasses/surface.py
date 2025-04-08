from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_type import SurfaceType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Surface(SurfaceType):
    """A Surface is a 2-dimensional primitive and is composed of one or more
    surface patches as specified in ISO 19107:2003, 6.3.17.1.

    The surface patches are connected to one another. patches
    encapsulates the patches of the surface.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
