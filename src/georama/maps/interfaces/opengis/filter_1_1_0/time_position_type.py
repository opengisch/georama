from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod, XmlTime

from georama.maps.interfaces.opengis.filter_1_1_0.time_indeterminate_value_type import (
    TimeIndeterminateValueType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TimePositionType:
    """Direct representation of a temporal position.

    Indeterminate time values are also allowed, as described in ISO
    19108. The indeterminatePosition attribute can be used alone or it
    can qualify a specific value for temporal position (e.g. before
    2002-12, after 1019624400). For time values that identify position
    within a calendar, the calendarEraName attribute provides the name
    of the calendar era to which the date is referenced (e.g. the Meiji
    era of the Japanese calendar).
    """

    value: Union[XmlDate, XmlPeriod, XmlTime, XmlDateTime, str, Decimal] = field(default="")
    frame: str = field(
        default="#ISO-8601",
        metadata={
            "type": "Attribute",
        },
    )
    calendar_era_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "calendarEraName",
            "type": "Attribute",
        },
    )
    indeterminate_position: Optional[TimeIndeterminateValueType] = field(
        default=None,
        metadata={
            "name": "indeterminatePosition",
            "type": "Attribute",
        },
    )
