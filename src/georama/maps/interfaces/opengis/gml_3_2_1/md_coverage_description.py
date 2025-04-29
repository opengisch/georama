from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.md_coverage_description_type import (
    MdCoverageDescriptionType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdCoverageDescription(MdCoverageDescriptionType):
    class Meta:
        name = "MD_CoverageDescription"
        namespace = "http://www.isotc211.org/2005/gmd"
