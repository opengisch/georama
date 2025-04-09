from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polyhedral_surface_type import (
    PolyhedralSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolyhedralSurface(PolyhedralSurfaceType):
    """A polyhedral surface is a surface composed of polygon patches connected
    along their common boundary curves.

    This differs from the surface type only in the restriction on the
    types of surface patches acceptable. polygonPatches encapsulates the
    polygon patches of the polyhedral surface.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
