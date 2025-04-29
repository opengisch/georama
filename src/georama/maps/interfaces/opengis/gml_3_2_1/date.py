from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate, XmlPeriod

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class Date:
    class Meta:
        nillable = True
        namespace = "http://www.isotc211.org/2005/gco"

    value: Optional[Union[XmlDate, XmlPeriod]] = field(
        default=None,
        metadata={
            "nillable": True,
        },
    )
