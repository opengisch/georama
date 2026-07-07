from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_coverage_description_type import (
    MdCoverageDescriptionType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdCoverageDescription(MdCoverageDescriptionType):
    class Meta:
        name = "MD_CoverageDescription"
        namespace = "http://www.isotc211.org/2005/gmd"
