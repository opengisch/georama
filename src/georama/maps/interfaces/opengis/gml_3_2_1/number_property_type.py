from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.decimal import DecimalType
from georama.maps.interfaces.opengis.gml_3_2_1.integer import Integer
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.real import Real

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class NumberPropertyType:
    class Meta:
        name = "Number_PropertyType"

    real: Real | None = field(
        default=None,
        metadata={
            "name": "Real",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    decimal: DecimalType | None = field(
        default=None,
        metadata={
            "name": "Decimal",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    integer: Integer | None = field(
        default=None,
        metadata={
            "name": "Integer",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
        },
    )
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
