from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Origin:
    """
    The date and time origin of this temporal datum.
    """

    class Meta:
        name = "origin"
        namespace = "http://www.opengis.net/gml"

    value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
