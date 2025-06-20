from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ColumnIndex:
    """
    Column number of this covariance element value.
    """

    class Meta:
        name = "columnIndex"
        namespace = "http://www.opengis.net/gml"

    value: Optional[int] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
