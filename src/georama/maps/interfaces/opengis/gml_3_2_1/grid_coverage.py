from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.discrete_coverage_type import (
    DiscreteCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridCoverage(DiscreteCoverageType):
    """A gml:GriddedCoverage is a discrete point coverage in which the domain set
    is a geometric grid of points.

    Note that this is the same as the gml:MultiPointCoverage except that
    we have a gml:Grid to describe the domain. The simple gridded
    coverage is not geometrically referenced and hence no geometric
    positions are assignable to the points in the grid. Such geometric
    positioning is introduced in the gml:RectifiedGridCoverage.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
