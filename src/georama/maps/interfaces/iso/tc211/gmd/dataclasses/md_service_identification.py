from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_service_identification_type import (
    MdServiceIdentificationType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdServiceIdentification(MdServiceIdentificationType):
    class Meta:
        name = "MD_ServiceIdentification"
        namespace = "http://www.isotc211.org/2005/gmd"
