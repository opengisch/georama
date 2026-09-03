from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.envelope import Envelope
from georama.maps.interfaces.opengis.filter_1_1_0.envelope_with_time_period import (
    EnvelopeWithTimePeriod,
)
from georama.maps.interfaces.opengis.filter_1_1_0.property_name import PropertyName
from georama.maps.interfaces.opengis.filter_1_1_0.spatial_ops_type import SpatialOpsType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class Bboxtype(SpatialOpsType):
    class Meta:
        name = "BBOXType"

    property_name: PropertyName | None = field(
        default=None,
        metadata={
            "name": "PropertyName",
            "type": "Element",
            "namespace": "http://www.opengis.net/ogc",
        },
    )
    envelope_with_time_period_or_envelope: EnvelopeWithTimePeriod | Envelope | None = (
        field(
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
                ),
            },
        )
    )
