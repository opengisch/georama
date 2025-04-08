from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_maintenance_information_type import (
    MdMaintenanceInformationType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMaintenanceInformation(MdMaintenanceInformationType):
    class Meta:
        name = "MD_MaintenanceInformation"
        namespace = "http://www.isotc211.org/2005/gmd"
