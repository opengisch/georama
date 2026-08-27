from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.md_imaging_condition_code import (
    MdImagingConditionCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdImagingConditionCodePropertyType:
    class Meta:
        name = "MD_ImagingConditionCode_PropertyType"

    md_imaging_condition_code: MdImagingConditionCode | None = field(
        default=None,
        metadata={
            "name": "MD_ImagingConditionCode",
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
