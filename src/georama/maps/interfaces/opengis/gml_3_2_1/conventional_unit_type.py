from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.conversion_to_preferred_unit import (
    ConversionToPreferredUnit,
)
from georama.maps.interfaces.opengis.gml_3_2_1.derivation_unit_term import (
    DerivationUnitTerm,
)
from georama.maps.interfaces.opengis.gml_3_2_1.rough_conversion_to_preferred_unit import (
    RoughConversionToPreferredUnit,
)
from georama.maps.interfaces.opengis.gml_3_2_1.unit_definition_type import (
    UnitDefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ConventionalUnitType(UnitDefinitionType):
    conversion_to_preferred_unit: ConversionToPreferredUnit | None = field(
        default=None,
        metadata={
            "name": "conversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rough_conversion_to_preferred_unit: RoughConversionToPreferredUnit | None = field(
        default=None,
        metadata={
            "name": "roughConversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derivation_unit_term: list[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
