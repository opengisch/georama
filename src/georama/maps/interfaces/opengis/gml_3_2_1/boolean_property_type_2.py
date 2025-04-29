from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.boolean_2 import Boolean2

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class BooleanPropertyType2:
    class Meta:
        name = "Boolean_PropertyType"

    boolean: Optional[Boolean2] = field(
        default=None,
        metadata={
            "name": "Boolean",
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
