from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.increment_order import (
    IncrementOrder,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sequence_rule_enumeration import (
    SequenceRuleEnumeration,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SequenceRuleType:
    """The gml:SequenceRuleType is derived from the gml:SequenceRuleEnumeration
    through the addition of an axisOrder attribute.

    The gml:SequenceRuleEnumeration is an enumerated type. The rule
    names are defined in ISO 19123. If no rule name is specified the
    default is “Linear”.
    """

    value: Optional[SequenceRuleEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
    order: Optional[IncrementOrder] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    axis_order: List[str] = field(
        default_factory=list,
        metadata={
            "name": "axisOrder",
            "type": "Attribute",
            "pattern": r"[\+\-][1-9][0-9]*",
            "tokens": True,
        },
    )
