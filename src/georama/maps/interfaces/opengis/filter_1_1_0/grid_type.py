from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometry_type import (
    AbstractGeometryType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.grid_limits_type import GridLimitsType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridType(AbstractGeometryType):
    """
    An unrectified grid, which is a network composed of two or more sets of equally
    spaced parallel lines in which the members of each set intersect the members of
    the other sets at right angles.
    """

    limits: GridLimitsType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    axis_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "axisName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    dimension: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
