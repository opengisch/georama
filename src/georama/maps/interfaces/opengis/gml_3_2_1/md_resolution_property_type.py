from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.gml_3_2_1.md_resolution import MdResolution
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdResolutionPropertyType:
    class Meta:
        name = "MD_Resolution_PropertyType"

    md_resolution: Optional[MdResolution] = field(
        default=None,
        metadata={
            "name": "MD_Resolution",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )
