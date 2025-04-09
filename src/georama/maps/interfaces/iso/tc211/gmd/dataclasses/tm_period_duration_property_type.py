from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.tm_period_duration import (
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
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
