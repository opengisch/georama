from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.country import Country
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CountryPropertyType:
    class Meta:
        name = "Country_PropertyType"

    country: Country | None = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
