from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.sequence_rule_type import (
    SequenceRuleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridFunctionType:
    """Defines how values in the domain are mapped to the range set.

    The start point and the sequencing rule are specified here.

    :ivar sequence_rule: If absent, the implied value is "Linear".
    :ivar start_point: Index position of the first grid post, which must
        lie somwhere in the GridEnvelope.  If absent, the startPoint is
        equal to the value of gridEnvelope::low from the grid
        definition.
    """

    sequence_rule: Optional[SequenceRuleType] = field(
        default=None,
        metadata={
            "name": "sequenceRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    start_point: list[int] = field(
        default_factory=list,
        metadata={
            "name": "startPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "tokens": True,
        },
    )
