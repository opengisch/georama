from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.unlimited_integer import UnlimitedInteger

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class UnlimitedIntegerPropertyType:
    class Meta:
        name = "UnlimitedInteger_PropertyType"

    unlimited_integer: Optional[UnlimitedInteger] = field(
        default=None,
        metadata={
            "name": "UnlimitedInteger",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
            "nillable": True,
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
