from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class Duration:
    """
    Gml:duration conforms to the ISO 8601 syntax for temporal length as implemented
    by the XML Schema duration type.
    """

    class Meta:
        name = "duration"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
