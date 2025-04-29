from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.md_browse_graphic_type import (
    MdBrowseGraphicType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdBrowseGraphic(MdBrowseGraphicType):
    class Meta:
        name = "MD_BrowseGraphic"
        namespace = "http://www.isotc211.org/2005/gmd"
