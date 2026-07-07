from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.md_medium_type import MdMediumType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdMedium(MdMediumType):
    class Meta:
        name = "MD_Medium"
        namespace = "http://www.isotc211.org/2005/gmd"
