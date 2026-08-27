from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.envelope import Envelope
from georama.maps.interfaces.opengis.gml_3_2_1.envelope_with_time_period import (
    EnvelopeWithTimePeriod,
)
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.null import Null

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BoundingShapeType:
    envelope_with_time_period: EnvelopeWithTimePeriod | None = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    envelope: Envelope | None = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    null: Null | None = field(
        default=None,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
