from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.domain_set_type import (
    DomainSetType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPointDomainType(DomainSetType):
    rectified_grid: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    grid: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    geometric_complex: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    multi_surface: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    multi_geometry: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    composite_solid: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    solid: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    composite_surface: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    orientable_surface: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    tin: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    triangulated_surface: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    polyhedral_surface: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    surface: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    polygon: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    composite_curve: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    orientable_curve: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    curve: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    line_string: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    point: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    time_topology_complex: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    time_edge: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    time_node: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    time_period: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    time_instant: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
