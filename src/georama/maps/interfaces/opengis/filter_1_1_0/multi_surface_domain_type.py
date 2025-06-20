from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.domain_set_type import DomainSetType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceDomainType(DomainSetType):
    multi_line_string: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_polygon: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_point: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_geometry: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    rectified_grid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    grid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    geometric_complex: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ring: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    linear_ring: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    solid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    composite_solid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    orientable_surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    tin: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    triangulated_surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    polyhedral_surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    composite_surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    polygon: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    orientable_curve: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    curve: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    composite_curve: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    line_string: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    point: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_topology_complex: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_edge: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_node: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_period: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_instant: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
