from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SourceDimensions:
    """
    Gml:sourceDimensions is the number of dimensions in the source CRS of this
    operation method.
    """

    class Meta:
        name = "sourceDimensions"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
