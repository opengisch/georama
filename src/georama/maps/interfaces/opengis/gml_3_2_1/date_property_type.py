from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.date import Date
from georama.maps.interfaces.opengis.gml_3_2_1.date_time import DateTime

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class DatePropertyType:
    class Meta:
        name = "Date_PropertyType"

    date: Optional[Date] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "nillable": True,
        },
    )
    date_time: Optional[DateTime] = field(
        default=None,
        metadata={
            "name": "DateTime",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
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
