from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class SequenceRuleEnumeration(Enum):
    LINEAR = "Linear"
    BOUSTROPHEDONIC = "Boustrophedonic"
    CANTOR_DIAGONAL = "Cantor-diagonal"
    SPIRAL = "Spiral"
    MORTON = "Morton"
    HILBERT = "Hilbert"
