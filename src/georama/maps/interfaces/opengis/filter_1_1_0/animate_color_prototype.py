from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.animate_color_prototype_accumulate import (
    AnimateColorPrototypeAccumulate,
)
from georama.maps.interfaces.opengis.filter_1_1_0.animate_color_prototype_additive import (
    AnimateColorPrototypeAdditive,
)
from georama.maps.interfaces.opengis.filter_1_1_0.animate_color_prototype_attribute_type import (
    AnimateColorPrototypeAttributeType,
)

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


@dataclass
class AnimateColorPrototype:
    class Meta:
        name = "animateColorPrototype"

    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
            "required": True,
        },
    )
    attribute_type: AnimateColorPrototypeAttributeType = field(
        default=AnimateColorPrototypeAttributeType.AUTO,
        metadata={
            "name": "attributeType",
            "type": "Attribute",
        },
    )
    additive: AnimateColorPrototypeAdditive = field(
        default=AnimateColorPrototypeAdditive.REPLACE,
        metadata={
            "type": "Attribute",
        },
    )
    accumulate: AnimateColorPrototypeAccumulate = field(
        default=AnimateColorPrototypeAccumulate.NONE,
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
