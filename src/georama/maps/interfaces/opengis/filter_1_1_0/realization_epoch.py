from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RealizationEpoch:
    """The time after which this datum definition is valid.

    This time may be precise (e.g. 1997.0 for IRTF97) or merely a year
    (e.g. 1983 for NAD83). In the latter case, the epoch usually refers
    to the year in which a major recalculation of the geodetic control
    network, underlying the datum, was executed or initiated. An old
    datum can remain valid after a new datum is defined. Alternatively,
    a datum may be superseded by a later datum, in which case the
    realization epoch for the new datum defines the upper limit for the
    validity of the superseded datum.
    """

    class Meta:
        name = "realizationEpoch"
        namespace = "http://www.opengis.net/gml"

    value: Optional[XmlDate] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
