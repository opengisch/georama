from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.md_metadata_extension_information_type import (
    MdMetadataExtensionInformationType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMetadataExtensionInformation(MdMetadataExtensionInformationType):
    class Meta:
        name = "MD_MetadataExtensionInformation"
        namespace = "http://www.isotc211.org/2005/gmd"
