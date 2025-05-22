from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.opengis.gml_3_2_1.ci_date_type_code import CiDateTypeCode
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class CiDateTypeCodePropertyType:
    class Meta:
        name = "CI_DateTypeCode_PropertyType"

    ci_date_type_code: Optional[CiDateTypeCode] = field(
        default=None,
        metadata={
            "name": "CI_DateTypeCode",
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
