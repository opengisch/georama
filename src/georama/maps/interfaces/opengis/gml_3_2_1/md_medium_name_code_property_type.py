from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_medium_name_code import (
    MdMediumNameCode,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMediumNameCodePropertyType:
    class Meta:
        name = "MD_MediumNameCode_PropertyType"

    md_medium_name_code: Optional[MdMediumNameCode] = field(
        default=None,
        metadata={
            "name": "MD_MediumNameCode",
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
