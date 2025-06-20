from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.surface_patch_array_property_type import (
    SurfacePatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PolygonPatchArrayPropertyType(SurfacePatchArrayPropertyType):
    """
    This type defines a container for an array of polygon patches.
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
    triangle: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
