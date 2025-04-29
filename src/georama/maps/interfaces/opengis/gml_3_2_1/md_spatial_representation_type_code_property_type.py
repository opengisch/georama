from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_spatial_representation_type_code import (
    MdSpatialRepresentationTypeCode,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdSpatialRepresentationTypeCodePropertyType:
    class Meta:
        name = "MD_SpatialRepresentationTypeCode_PropertyType"

    md_spatial_representation_type_code: Optional[MdSpatialRepresentationTypeCode] = field(
        default=None,
        metadata={
            "name": "MD_SpatialRepresentationTypeCode",
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
