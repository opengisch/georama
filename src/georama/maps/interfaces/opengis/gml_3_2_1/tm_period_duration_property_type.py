from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.tm_period_duration import (
    TmPeriodDuration,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gts"


@dataclass
class TmPeriodDurationPropertyType:
    class Meta:
        name = "TM_PeriodDuration_PropertyType"

    tm_period_duration: Optional[TmPeriodDuration] = field(
        default=None,
        metadata={
            "name": "TM_PeriodDuration",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gts",
        },
    )
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
