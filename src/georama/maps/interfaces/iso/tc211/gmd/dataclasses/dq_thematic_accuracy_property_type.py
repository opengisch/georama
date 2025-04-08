from dataclasses import dataclass, field
from typing import Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_non_quantitative_attribute_accuracy import (
    DqNonQuantitativeAttributeAccuracy,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_quantitative_attribute_accuracy import (
    DqQuantitativeAttributeAccuracy,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dq_thematic_classification_correctness import (
    DqThematicClassificationCorrectness,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class DqThematicAccuracyPropertyType:
    class Meta:
        name = "DQ_ThematicAccuracy_PropertyType"

    dq_thematic_classification_correctness: Optional[
        DqThematicClassificationCorrectness
    ] = field(
        default=None,
        metadata={
            "name": "DQ_ThematicClassificationCorrectness",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_non_quantitative_attribute_accuracy: Optional[
        DqNonQuantitativeAttributeAccuracy
    ] = field(
        default=None,
        metadata={
            "name": "DQ_NonQuantitativeAttributeAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    dq_quantitative_attribute_accuracy: Optional[DqQuantitativeAttributeAccuracy] = field(
        default=None,
        metadata={
            "name": "DQ_QuantitativeAttributeAccuracy",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    type_value: str = field(
        init=False,
        default="simple",
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
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
