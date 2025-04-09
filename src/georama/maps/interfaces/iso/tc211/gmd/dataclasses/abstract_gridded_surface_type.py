from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gridded_surface_type_rows import (
    AbstractGriddedSurfaceTypeRows,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_parametric_curve_surface_type import (
    AbstractParametricCurveSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGriddedSurfaceType(AbstractParametricCurveSurfaceType):
    rows: Optional[AbstractGriddedSurfaceTypeRows] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    rows_attribute: Optional[int] = field(
        default=None,
        metadata={
            "name": "rows",
            "type": "Attribute",
        },
    )
    columns: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
