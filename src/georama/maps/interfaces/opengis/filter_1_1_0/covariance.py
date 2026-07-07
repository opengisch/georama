from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Covariance:
    """
    Value of covariance matrix element.
    """

    class Meta:
        name = "covariance"
        namespace = "http://www.opengis.net/gml"

    value: Optional[float] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
