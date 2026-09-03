from dataclasses import dataclass, field

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
    to: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    from_value: str | None = field(
        default=None,
        metadata={
            "name": "from",
            "type": "Attribute",
        },
    )
    by: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    values: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    origin: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
