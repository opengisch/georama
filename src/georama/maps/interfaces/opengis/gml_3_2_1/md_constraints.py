from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.md_constraints_type import (
    MdConstraintsType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdConstraints(MdConstraintsType):
    class Meta:
        name = "MD_Constraints"
        namespace = "http://www.isotc211.org/2005/gmd"
