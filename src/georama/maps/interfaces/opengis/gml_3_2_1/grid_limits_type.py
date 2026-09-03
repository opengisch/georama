from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.grid_envelope_type import (
    GridEnvelopeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridLimitsType:
    grid_envelope: GridEnvelopeType | None = field(
        default=None,
        metadata={
            "name": "GridEnvelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
