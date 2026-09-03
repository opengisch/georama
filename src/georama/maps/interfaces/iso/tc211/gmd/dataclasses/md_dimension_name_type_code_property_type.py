from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_dimension_name_type_code import (
    MdDimensionNameTypeCode,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDimensionNameTypeCodePropertyType:
    class Meta:
        name = "MD_DimensionNameTypeCode_PropertyType"

    md_dimension_name_type_code: MdDimensionNameTypeCode | None = field(
        default=None,
        metadata={
            "name": "MD_DimensionNameTypeCode",
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
