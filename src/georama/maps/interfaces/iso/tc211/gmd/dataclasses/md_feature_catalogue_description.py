from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_feature_catalogue_description_type import (
    MdFeatureCatalogueDescriptionType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdFeatureCatalogueDescription(MdFeatureCatalogueDescriptionType):
    class Meta:
        name = "MD_FeatureCatalogueDescription"
        namespace = "http://www.isotc211.org/2005/gmd"
