from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.md_maintenance_frequency_code import (
    MdMaintenanceFrequencyCode,
)
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMaintenanceFrequencyCodePropertyType:
    class Meta:
        name = "MD_MaintenanceFrequencyCode_PropertyType"

    md_maintenance_frequency_code: MdMaintenanceFrequencyCode | None = field(
        default=None,
        metadata={
            "name": "MD_MaintenanceFrequencyCode",
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
