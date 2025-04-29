from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.isotc211.org/2005/gts"


@dataclass
class TmPeriodDuration:
    class Meta:
        name = "TM_PeriodDuration"
        namespace = "http://www.isotc211.org/2005/gts"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
