from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometry_type import (
    AbstractGeometryType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.grid_limits_type import (
    GridLimitsType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridType(AbstractGeometryType):
    limits: GridLimitsType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    axis_labels: list[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        },
    )
    axis_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "axisName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dimension: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
