from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.surface_patch_array_property_type import (
    SurfacePatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TrianglePatchArrayPropertyType(SurfacePatchArrayPropertyType):
    """
    This type defines a container for an array of triangle patches.
    """

    sphere: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    cylinder: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    cone: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    rectangle: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    polygon_patch: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
