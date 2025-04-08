from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.rectified_grid_type import (
    RectifiedGridType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectifiedGrid(RectifiedGridType):
    """A rectified grid is a grid for which there is an affine transformation
    between the grid coordinates and the coordinates of an external coordinate
    reference system.

    It is defined by specifying the position (in some geometric space)
    of the grid “origin” and of the vectors that specify the post
    locations. Note that the grid limits (post indexes) and axis name
    properties are inherited from gml:GridType and that
    gml:RectifiedGrid adds a gml:origin property (contains or references
    a gml:Point) and a set of gml:offsetVector properties.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
