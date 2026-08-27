from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.animate_prototype_accumulate import (
    AnimatePrototypeAccumulate,
)
from georama.maps.interfaces.opengis.filter_1_1_0.animate_prototype_additive import (
    AnimatePrototypeAdditive,
)
from georama.maps.interfaces.opengis.filter_1_1_0.animate_prototype_attribute_type import (
    AnimatePrototypeAttributeType,
)

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


@dataclass
class AnimatePrototype:
    class Meta:
        name = "animatePrototype"

    attribute_name: str | None = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
            "required": True,
        },
    )
    attribute_type: AnimatePrototypeAttributeType = field(
        default=AnimatePrototypeAttributeType.AUTO,
        metadata={
            "name": "attributeType",
            "type": "Attribute",
        },
    )
    additive: AnimatePrototypeAdditive = field(
        default=AnimatePrototypeAdditive.REPLACE,
        metadata={
            "type": "Attribute",
        },
    )
    accumulate: AnimatePrototypeAccumulate = field(
        default=AnimatePrototypeAccumulate.NONE,
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
