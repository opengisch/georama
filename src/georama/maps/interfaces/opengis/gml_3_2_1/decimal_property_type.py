from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.decimal import DecimalType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class DecimalPropertyType:
    class Meta:
        name = "Decimal_PropertyType"

    decimal: Optional[DecimalType] = field(
        default=None,
        metadata={
            "name": "Decimal",
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
