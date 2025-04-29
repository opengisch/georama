from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.scale import Scale

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class ScalePropertyType:
    class Meta:
        name = "Scale_PropertyType"

    scale: Optional[Scale] = field(
        default=None,
        metadata={
            "name": "Scale",
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
