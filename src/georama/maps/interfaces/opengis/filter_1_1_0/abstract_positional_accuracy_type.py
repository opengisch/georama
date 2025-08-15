from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.measure_description import (
    MeasureDescription,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractPositionalAccuracyType:
    """
    Position error estimate (or accuracy) data.
    """

    measure_description: Optional[MeasureDescription] = field(
        default=None,
        metadata={
            "name": "measureDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
