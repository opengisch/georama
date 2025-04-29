from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class RealizationEpoch:
    """Gml:realizationEpoch is the time after which this datum definition is valid.

    See ISO 19111 Table 32 for details.
    """

    class Meta:
        name = "realizationEpoch"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
