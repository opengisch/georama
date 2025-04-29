from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_dimension_name_type_code import (
    MdDimensionNameTypeCode,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDimensionNameTypeCodePropertyType:
    class Meta:
        name = "MD_DimensionNameTypeCode_PropertyType"

    md_dimension_name_type_code: Optional[MdDimensionNameTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_DimensionNameTypeCode",
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
