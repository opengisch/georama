from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gridded_surface_type import (
    AbstractGriddedSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGriddedSurface(AbstractGriddedSurfaceType):
    """If provided, rows gives the number of rows, columns the number of columns in
    the parameter grid.

    The parameter grid is represented by an instance of the
    gml:PointGrid group. The element provides a substitution group head
    for the surface patches based on a grid. All derived subtypes shall
    conform to the constraints specified in ISO 19107:2003, 6.4.41.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
