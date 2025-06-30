from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_datum_type import (
    AbstractDatumType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TemporalDatumBaseType(AbstractDatumType):
    """Partially defines the origin of a temporal coordinate reference system.

    This type restricts the AbstractDatumType to remove the
    "anchorPoint" and "realizationEpoch" elements.

    :ivar remarks: Comments on this reference system, including source
        information.
    :ivar anchor_point:
    :ivar realization_epoch:
    :ivar description:
    :ivar choice_1:
    """

    remarks: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    anchor_point: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    realization_epoch: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    description: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
