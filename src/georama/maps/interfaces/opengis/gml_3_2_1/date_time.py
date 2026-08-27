from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class DateTime:
    class Meta:
        namespace = "http://www.isotc211.org/2005/gco"

    value: XmlDateTime | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
