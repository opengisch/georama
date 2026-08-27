from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.grid_envelope_type import (
    GridEnvelopeType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridLimitsType:
    grid_envelope: GridEnvelopeType | None = field(
        default=None,
        metadata={
            "name": "GridEnvelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
