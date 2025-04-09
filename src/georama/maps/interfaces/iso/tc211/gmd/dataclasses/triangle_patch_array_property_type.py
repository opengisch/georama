from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_patch_array_property_type import (
    SurfacePatchArrayPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TrianglePatchArrayPropertyType(SurfacePatchArrayPropertyType):
    """
    Gml:TrianglePatchArrayPropertyType provides a container for an array of
    triangle patches.
    """

    sphere: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    cylinder: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    cone: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    rectangle: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    polygon_patch: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
