from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.conversion_to_preferred_unit import (
    ConversionToPreferredUnit,
)
from georama.maps.interfaces.opengis.filter_1_1_0.derivation_unit_term import (
    DerivationUnitTerm,
)
from georama.maps.interfaces.opengis.filter_1_1_0.rough_conversion_to_preferred_unit import (
    RoughConversionToPreferredUnit,
)
from georama.maps.interfaces.opengis.filter_1_1_0.unit_definition_type import (
    UnitDefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConventionalUnitType(UnitDefinitionType):
    """Definition of a unit of measure which is related to a preferred unit for
    this quantity type through a conversion formula.

    A method for deriving this unit by algebraic combination of more
    primitive units, may also be provided.
    """

    conversion_to_preferred_unit: Optional[ConversionToPreferredUnit] = field(
        default=None,
        metadata={
            "name": "conversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rough_conversion_to_preferred_unit: Optional[RoughConversionToPreferredUnit] = field(
        default=None,
        metadata={
            "name": "roughConversionToPreferredUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derivation_unit_term: list[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
