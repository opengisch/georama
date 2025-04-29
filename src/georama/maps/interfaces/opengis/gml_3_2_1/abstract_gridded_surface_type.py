from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_gridded_surface_type_rows import (
    AbstractGriddedSurfaceTypeRows,
)
from georama.maps.interfaces.opengis.gml_3_2_1.abstract_parametric_curve_surface_type import (
    AbstractParametricCurveSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGriddedSurfaceType(AbstractParametricCurveSurfaceType):
    rows: Optional[AbstractGriddedSurfaceTypeRows] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
