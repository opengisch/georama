from enum import Enum

__NAMESPACE__ = "http://www.opengis.net/gml"


class SequenceRuleNames(Enum):
    """
    List of codes (adopted from ISO 19123 Annex C) that identifies the rule for
    traversing a grid to correspond with the sequence of members of the rangeSet.
    """

    LINEAR = "Linear"
    BOUSTROPHEDONIC = "Boustrophedonic"
    CANTOR_DIAGONAL = "Cantor-diagonal"
    SPIRAL = "Spiral"
    MORTON = "Morton"
    HILBERT = "Hilbert"
