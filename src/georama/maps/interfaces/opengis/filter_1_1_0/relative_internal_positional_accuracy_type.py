from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_positional_accuracy_type import (
    AbstractPositionalAccuracyType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.result import Result

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class RelativeInternalPositionalAccuracyType(AbstractPositionalAccuracyType):
    """
    Closeness of the relative positions of two or more positions to their
    respective relative positions accepted as or being true.
    """

    result: Result | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
