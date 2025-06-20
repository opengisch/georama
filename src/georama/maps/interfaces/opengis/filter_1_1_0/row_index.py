from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RowIndex:
    """
    Row number of this covariance element value.
    """

    class Meta:
        name = "rowIndex"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
