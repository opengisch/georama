from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.grid_coverage_type import (
    GridCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridCoverage(GridCoverageType):
    """A gml:GriddedCoverage is a discrete point coverage in which the domain set
    is a geometric grid of points.

    Note that this is the same as the gml:MultiPointCoverage except that
    we have a gml:gridDomain property to describe the domain. The simple
    gridded coverage is not geometrically referenced and hence no
    geometric positions are assignable to the points in the grid. Such
    geometric positioning is introduced in the
    gml:RectifiedGridCoverage.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
