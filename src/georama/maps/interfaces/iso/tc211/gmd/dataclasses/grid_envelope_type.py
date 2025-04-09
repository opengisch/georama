from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridEnvelopeType:
    low: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        },
    )
    high: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        },
    )
