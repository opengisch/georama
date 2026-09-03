from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_geometry_type import (
    AbstractGeometryType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.grid_limits_type import GridLimitsType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridType(AbstractGeometryType):
    limits: GridLimitsType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    axis_labels: list[str] = field(
        default_factory=list,
        metadata={
            "name": "axisLabels",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "tokens": True,
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
    dimension: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
