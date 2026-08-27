from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_keyword_type_code import (
    MdKeywordTypeCode,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdKeywordTypeCodePropertyType:
    class Meta:
        name = "MD_KeywordTypeCode_PropertyType"

    md_keyword_type_code: MdKeywordTypeCode | None = field(
        default=None,
        metadata={
            "name": "MD_KeywordTypeCode",
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
