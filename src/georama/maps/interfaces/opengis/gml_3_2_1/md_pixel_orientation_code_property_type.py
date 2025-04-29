from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_pixel_orientation_code import (
    MdPixelOrientationCode,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdPixelOrientationCodePropertyType:
    class Meta:
        name = "MD_PixelOrientationCode_PropertyType"

    md_pixel_orientation_code: Optional[MdPixelOrientationCode] = field(
        default=None,
        metadata={
            "name": "MD_PixelOrientationCode",
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
