from dataclasses import dataclass

from georama.maps.interfaces.opengis.gml_3_2_1.derivation_unit_term_type import (
    DerivationUnitTermType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivationUnitTerm(DerivationUnitTermType):
    """A set of gml:derivationUnitTerm elements describes a derived unit of
    measure.

    Each element carries an integer exponent.  The terms are combined by
    raising each referenced unit to the power of its exponent and
    forming the product. This unit term references another unit of
    measure (uom) and provides an integer exponent applied to that unit
    in defining the compound unit. The exponent may be positive or
    negative, but not zero.
    """

    class Meta:
        name = "derivationUnitTerm"
        namespace = "http://www.opengis.net/gml/3.2"
