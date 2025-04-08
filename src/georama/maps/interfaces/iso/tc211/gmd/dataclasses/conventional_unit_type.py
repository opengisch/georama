from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.conversion_to_preferred_unit import (
    ConversionToPreferredUnit,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.derivation_unit_term import (
    DerivationUnitTerm,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.rough_conversion_to_preferred_unit import (
    RoughConversionToPreferredUnit,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.unit_definition_type import (
    UnitDefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConventionalUnitType(UnitDefinitionType):
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
    derivation_unit_term: List[DerivationUnitTerm] = field(
        default_factory=list,
        metadata={
            "name": "derivationUnitTerm",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
