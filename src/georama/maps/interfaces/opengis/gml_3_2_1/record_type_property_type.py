from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.record_type import RecordType

__NAMESPACE__ = "http://www.isotc211.org/2005/gco"


@dataclass
class RecordTypePropertyType:
    class Meta:
        name = "RecordType_PropertyType"

    record_type: Optional[RecordType] = field(
        default=None,
        metadata={
            "name": "RecordType",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gco",
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
