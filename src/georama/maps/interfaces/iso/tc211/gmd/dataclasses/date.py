from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlPeriod

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Date:
    class Meta:
        nillable = True
        namespace = "http://www.isotc211.org/2005/gco"

    value: XmlDate | XmlPeriod | None = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )
