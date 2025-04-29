from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.integer import Integer

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class IntegerPropertyType:
    class Meta:
        name = "Integer_PropertyType"

    integer: Optional[Integer] = field(
        default=None,
        metadata={
            "name": "Integer",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
