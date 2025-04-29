from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.md_scope_description_type import (
    MdScopeDescriptionType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdScopeDescription(MdScopeDescriptionType):
    class Meta:
        name = "MD_ScopeDescription"
        namespace = "http://www.isotc211.org/2005/gmd"
