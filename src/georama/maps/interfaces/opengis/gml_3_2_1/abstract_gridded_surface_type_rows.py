from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_gridded_surface_type_rows_row import (
    AbstractGriddedSurfaceTypeRowsRow,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGriddedSurfaceTypeRows:
    class Meta:
        global_type = False

    row: list[AbstractGriddedSurfaceTypeRowsRow] = field(
        default_factory=list,
        metadata={
            "name": "Row",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
