from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.set_prototype_attribute_type import (
    SetPrototypeAttributeType,
)

__NAMESPACE__ = "http://www.w3.org/2001/SMIL20/"


@dataclass
class SetPrototype:
    class Meta:
        name = "setPrototype"

    attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "attributeName",
            "type": "Attribute",
            "required": True,
        },
    )
    attribute_type: SetPrototypeAttributeType = field(
        default=SetPrototypeAttributeType.AUTO,
        metadata={
            "name": "attributeType",
            "type": "Attribute",
        },
    )
    to: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
