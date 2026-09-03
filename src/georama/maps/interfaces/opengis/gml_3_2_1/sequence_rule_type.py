from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.increment_order import IncrementOrder
from georama.maps.interfaces.opengis.gml_3_2_1.sequence_rule_enumeration import (
    SequenceRuleEnumeration,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class SequenceRuleType:
    """The gml:SequenceRuleType is derived from the gml:SequenceRuleEnumeration
    through the addition of an axisOrder attribute.

    The gml:SequenceRuleEnumeration is an enumerated type. The rule
    names are defined in ISO 19123. If no rule name is specified the
    default is "Linear".
    """

    value: SequenceRuleEnumeration | None = field(
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
    axis_order: list[str] = field(
        default_factory=list,
        metadata={
            "name": "axisOrder",
            "type": "Attribute",
            "pattern": r"[\+\-][1-9][0-9]*",
            "tokens": True,
        },
    )
