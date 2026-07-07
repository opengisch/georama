from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.animate_motion_prototype_accumulate import (
    AnimateMotionPrototypeAccumulate,
)
from georama.maps.interfaces.opengis.filter_1_1_0.animate_motion_prototype_additive import (
    AnimateMotionPrototypeAdditive,
)

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


@dataclass
class AnimateMotionPrototype:
    class Meta:
        name = "animateMotionPrototype"

    additive: AnimateMotionPrototypeAdditive = field(
        default=AnimateMotionPrototypeAdditive.REPLACE,
        metadata={
            "type": "Attribute",
        },
    )
    accumulate: AnimateMotionPrototypeAccumulate = field(
        default=AnimateMotionPrototypeAccumulate.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    from_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        },
    )
    by: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    values: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    origin: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
