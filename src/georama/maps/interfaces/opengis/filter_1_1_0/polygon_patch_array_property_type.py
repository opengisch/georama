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

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
