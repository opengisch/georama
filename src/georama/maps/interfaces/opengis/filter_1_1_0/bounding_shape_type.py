from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.envelope import Envelope
from georama.maps.interfaces.opengis.filter_1_1_0.envelope_with_time_period import (
    EnvelopeWithTimePeriod,
)
from georama.maps.interfaces.opengis.filter_1_1_0.null import Null

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundingShapeType:
    """
    Bounding shape.
    """

    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    null: Optional[Null] = field(
        default=None,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
