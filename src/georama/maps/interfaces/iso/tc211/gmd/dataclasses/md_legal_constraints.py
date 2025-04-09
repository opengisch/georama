from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_legal_constraints_type import (
    MdLegalConstraintsType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdLegalConstraints(MdLegalConstraintsType):
    class Meta:
        name = "MD_LegalConstraints"
        namespace = "http://www.isotc211.org/2005/gmd"
