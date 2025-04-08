from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.rectified_grid_coverage_type import (
    RectifiedGridCoverageType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridCoverage(RectifiedGridCoverageType):
    """The gml:RectifiedGridCoverage is a discrete point coverage based on a
    rectified grid.

    It is similar to the grid coverage except that the points of the
    grid are geometrically referenced. The rectified grid coverage has a
    domain that is a gml:RectifiedGrid geometry. The coverage domain is
    described by gml:rectifiedGridDomain.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
