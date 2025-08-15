from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.md_obligation_code_type import (
    MdObligationCodeType,
)

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


@dataclass
class MdObligationCode:
    class Meta:
        name = "MD_ObligationCode"
        namespace = "http://www.isotc211.org/2005/gmd"

    value: Optional[MdObligationCodeType] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
