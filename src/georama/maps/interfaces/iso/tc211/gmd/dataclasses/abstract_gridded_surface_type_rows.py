from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gridded_surface_type_rows_row import (
    AbstractGriddedSurfaceTypeRowsRow,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGriddedSurfaceTypeRows:
    class Meta:
        global_type = False

    row: list[AbstractGriddedSurfaceTypeRowsRow] = field(
        default_factory=list,
        metadata={
            "name": "Row",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
