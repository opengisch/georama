from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.derivation_unit_term import (
    DerivationUnitTerm,
)
from georama.maps.interfaces.opengis.gml_3_2_1.unit_definition_type import (
    UnitDefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedUnitType(UnitDefinitionType):
    derivation_unit_term: list[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
