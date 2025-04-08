from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_geometry_type import (
    AbstractGeometryType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.grid_limits_type import (
    GridLimitsType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridType(AbstractGeometryType):
    limits: Optional[GridLimitsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    axis_labels: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        },
    )
    axis_name: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dimension: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
