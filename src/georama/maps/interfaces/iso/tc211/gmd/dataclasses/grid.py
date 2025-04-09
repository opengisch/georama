from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.grid_type import GridType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Grid(GridType):
    """The gml:Grid implicitly defines an unrectified grid, which is a network
    composed of two or more sets of curves in which the members of each set
    intersect the members of the other sets in an algorithmic way.

    The region of interest within the grid is given in terms of its
    gml:limits, being the grid coordinates of  diagonally opposed
    corners of a rectangular region.  gml:axisLabels is provided with a
    list of labels of the axes of the grid (gml:axisName has been
    deprecated). gml:dimension specifies the dimension of the grid. The
    gml:limits element contains a single gml:GridEnvelope. The gml:low
    and gml:high property elements of the envelope are each
    integerLists, which are coordinate tuples, the coordinates being
    measured as offsets from the origin of the grid along each axis, of
    the diagonally opposing corners of a “rectangular” region of
    interest.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
