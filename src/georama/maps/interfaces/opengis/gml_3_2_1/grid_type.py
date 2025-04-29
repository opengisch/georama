from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometry_type import (
    AbstractGeometryType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.grid_limits_type import GridLimitsType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridType(AbstractGeometryType):
    limits: Optional[GridLimitsType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    axis_labels: Optional[str] = field(
        default=None,
        metadata={
            "name": "axisLabels",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    axis_name: list[str] = field(
        default_factory=list,
        metadata={
            "name": "axisName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dimension: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
