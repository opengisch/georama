from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SourceDimensions:
    """
    Number of dimensions in the source CRS of this operation method.
    """

    class Meta:
        name = "sourceDimensions"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
