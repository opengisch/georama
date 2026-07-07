from dataclasses import dataclass, field
from typing import Optional, Union

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

    envelope_with_time_period_or_envelope_or_null: Optional[
        Union[EnvelopeWithTimePeriod, Envelope, Null]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EnvelopeWithTimePeriod",
                    "type": EnvelopeWithTimePeriod,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Envelope",
                    "type": Envelope,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Null",
                    "type": Null,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
