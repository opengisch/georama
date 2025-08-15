from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.derivation_unit_term_type import (
    DerivationUnitTermType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DerivationUnitTerm(DerivationUnitTermType):
    class Meta:
        name = "derivationUnitTerm"
        namespace = "http://www.opengis.net/gml"
