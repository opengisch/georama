from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.envelope_type import EnvelopeType
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_position_type import (
    TimePositionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EnvelopeWithTimePeriodType(EnvelopeType):
    begin_position: TimePositionType | None = field(
        default=None,
        metadata={
            "name": "beginPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    end_position: TimePositionType | None = field(
        default=None,
        metadata={
            "name": "endPosition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        },
    )
