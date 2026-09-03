from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gridded_surface_type_rows import (
    AbstractGriddedSurfaceTypeRows,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_parametric_curve_surface_type import (
    AbstractParametricCurveSurfaceType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGriddedSurfaceType(AbstractParametricCurveSurfaceType):
    rows: AbstractGriddedSurfaceTypeRows | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    rows_attribute: int | None = field(
        default=None,
        metadata={
            "name": "rows",
            "type": "Attribute",
        },
    )
    columns: int | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
