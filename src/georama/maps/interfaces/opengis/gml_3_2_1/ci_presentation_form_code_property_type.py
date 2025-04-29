from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.ci_presentation_form_code import (
    CiPresentationFormCode,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiPresentationFormCodePropertyType:
    class Meta:
        name = "CI_PresentationFormCode_PropertyType"

    ci_presentation_form_code: Optional[CiPresentationFormCode] = field(
        default=None,
        metadata={
            "name": "CI_PresentationFormCode",
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
