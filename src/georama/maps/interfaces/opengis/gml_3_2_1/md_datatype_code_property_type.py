from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_datatype_code import MdDatatypeCode

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdDatatypeCodePropertyType:
    class Meta:
        name = "MD_DatatypeCode_PropertyType"

    md_datatype_code: Optional[MdDatatypeCode] = field(
        default=None,
        metadata={
            "name": "MD_DatatypeCode",
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
