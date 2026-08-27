from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.md_obligation_code_type import (
    MdObligationCodeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdObligationCode:
    class Meta:
        name = "MD_ObligationCode"
        namespace = "http://www.isotc211.org/2005/gmd"

    value: MdObligationCodeType | None = field(
        default=None,
        metadata={
            "required": True,
        },
    )
