from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.increment_order import IncrementOrder
from georama.maps.interfaces.opengis.filter_1_1_0.sequence_rule_names import (
    SequenceRuleNames,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SequenceRuleType:
    value: SequenceRuleNames | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    order: IncrementOrder | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
