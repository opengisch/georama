from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.envelope_with_time_period_type import (
    EnvelopeWithTimePeriodType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EnvelopeWithTimePeriod(EnvelopeWithTimePeriodType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
