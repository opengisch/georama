from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_positional_accuracy_type import (
    AbstractPositionalAccuracyType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.result import Result

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbsoluteExternalPositionalAccuracyType(AbstractPositionalAccuracyType):
    """
    Closeness of reported coordinate values to values accepted as or being true.
    """

    result: Optional[Result] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
