from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_evaluation_method_type_code import (
    DqEvaluationMethodTypeCode,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqEvaluationMethodTypeCodePropertyType:
    class Meta:
        name = "DQ_EvaluationMethodTypeCode_PropertyType"

    dq_evaluation_method_type_code: DqEvaluationMethodTypeCode | None = field(
        default=None,
        metadata={
            "name": "DQ_EvaluationMethodTypeCode",
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
