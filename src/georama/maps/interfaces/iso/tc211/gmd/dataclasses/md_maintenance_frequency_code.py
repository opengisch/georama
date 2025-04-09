from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.code_list_value_type import (
    CodeListValueType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMaintenanceFrequencyCode(CodeListValueType):
    class Meta:
        name = "MD_MaintenanceFrequencyCode"
        namespace = "http://www.isotc211.org/2005/gmd"
