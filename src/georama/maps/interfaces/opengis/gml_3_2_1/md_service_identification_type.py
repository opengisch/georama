from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_md_identification_type import (
    AbstractMdIdentificationType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdServiceIdentificationType(AbstractMdIdentificationType):
    """
    See 19119 for further info.
    """

    class Meta:
        name = "MD_ServiceIdentification_Type"
