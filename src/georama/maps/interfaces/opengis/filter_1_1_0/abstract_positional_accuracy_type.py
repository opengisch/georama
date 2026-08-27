from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.measure_description import (
    MeasureDescription,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractPositionalAccuracyType:
    """
    Position error estimate (or accuracy) data.
    """

    measure_description: MeasureDescription | None = field(
        default=None,
        metadata={
            "name": "measureDescription",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
