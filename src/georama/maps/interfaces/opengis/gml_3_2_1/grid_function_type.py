from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.sequence_rule_type import (
    SequenceRuleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridFunctionType:
    sequence_rule: SequenceRuleType | None = field(
        default=None,
        metadata={
            "name": "sequenceRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    start_point: list[int] = field(
        default_factory=list,
        metadata={
            "name": "startPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "tokens": True,
        },
    )
