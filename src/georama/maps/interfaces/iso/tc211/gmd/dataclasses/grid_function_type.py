from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sequence_rule_type import (
    SequenceRuleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GridFunctionType:
    sequence_rule: SequenceRuleType | None = field(
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
