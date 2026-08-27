from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.envelope import Envelope
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.envelope_with_time_period import (
    EnvelopeWithTimePeriod,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.null import Null

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BoundingShapeType:
    envelope_with_time_period: EnvelopeWithTimePeriod | None = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope: Envelope | None = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    null: Null | None = field(
        default=None,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
