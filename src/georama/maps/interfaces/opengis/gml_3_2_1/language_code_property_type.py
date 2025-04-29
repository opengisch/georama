from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.language_code import LanguageCode

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class LanguageCodePropertyType:
    class Meta:
        name = "LanguageCode_PropertyType"

    language_code: Optional[LanguageCode] = field(
        default=None,
        metadata={
            "name": "LanguageCode",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
