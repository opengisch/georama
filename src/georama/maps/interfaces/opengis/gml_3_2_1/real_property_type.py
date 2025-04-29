from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.real import Real

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class RealPropertyType:
    class Meta:
        name = "Real_PropertyType"

    real: Optional[Real] = field(
        default=None,
        metadata={
            "name": "Real",
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
