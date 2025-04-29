from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.sequence_rule_type import (
    SequenceRuleType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class GridFunctionType:
    sequence_rule: Optional[SequenceRuleType] = field(
        default=None,
        metadata={
            "name": "sequenceRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    start_point: Optional[str] = field(
        default=None,
        metadata={
            "name": "startPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
