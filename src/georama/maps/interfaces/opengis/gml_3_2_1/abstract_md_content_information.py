from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_md_content_information_type import (
    AbstractMdContentInformationType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class AbstractMdContentInformation(AbstractMdContentInformationType):
    class Meta:
        name = "AbstractMD_ContentInformation"
        namespace = "http://www.isotc211.org/2005/gmd"
