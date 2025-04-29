from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.pt_free_text_type import PtFreeTextType

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class PtFreeText(PtFreeTextType):
    class Meta:
        name = "PT_FreeText"
        namespace = "http://www.isotc211.org/2005/gmd"
