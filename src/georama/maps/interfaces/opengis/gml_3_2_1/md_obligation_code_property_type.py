from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_obligation_code import (
    MdObligationCode,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdObligationCodePropertyType:
    class Meta:
        name = "MD_ObligationCode_PropertyType"

    md_obligation_code: Optional[MdObligationCode] = field(
        default=None,
        metadata={
            "name": "MD_ObligationCode",
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
