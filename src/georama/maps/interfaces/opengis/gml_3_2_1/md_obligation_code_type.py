from enum import Enum

__NAMESPACE__ = "http://www.isotc211.org/2005/gmd"


class MdObligationCodeType(Enum):
    MANDATORY = "mandatory"
    OPTIONAL = "optional"
    CONDITIONAL = "conditional"
