from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_classification_code import (
    MdClassificationCode,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdClassificationCodePropertyType:
    class Meta:
        name = "MD_ClassificationCode_PropertyType"

    md_classification_code: Optional[MdClassificationCode] = field(
        default=None,
        metadata={
            "name": "MD_ClassificationCode",
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
