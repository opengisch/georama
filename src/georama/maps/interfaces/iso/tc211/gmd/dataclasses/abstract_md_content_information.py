from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_md_content_information_type import (
    AbstractMdContentInformationType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractMdContentInformation(AbstractMdContentInformationType):
    class Meta:
        name = "AbstractMD_ContentInformation"
        namespace = "http://www.isotc211.org/2005/gmd"
