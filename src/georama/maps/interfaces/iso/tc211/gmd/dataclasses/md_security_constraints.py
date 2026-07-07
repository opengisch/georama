from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_security_constraints_type import (
    MdSecurityConstraintsType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdSecurityConstraints(MdSecurityConstraintsType):
    class Meta:
        name = "MD_SecurityConstraints"
        namespace = "http://www.isotc211.org/2005/gmd"
