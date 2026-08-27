from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.md_geometric_object_type_code import (
    MdGeometricObjectTypeCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdGeometricObjectTypeCodePropertyType:
    class Meta:
        name = "MD_GeometricObjectTypeCode_PropertyType"

    md_geometric_object_type_code: MdGeometricObjectTypeCode | None = field(
        default=None,
        metadata={
            "name": "MD_GeometricObjectTypeCode",
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
