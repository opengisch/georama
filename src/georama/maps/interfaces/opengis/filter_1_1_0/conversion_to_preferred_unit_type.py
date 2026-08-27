from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.formula_type import FormulaType
from georama.maps.interfaces.opengis.filter_1_1_0.unit_of_measure_type import (
    UnitOfMeasureType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConversionToPreferredUnitType(UnitOfMeasureType):
    """Relation of a unit to the preferred unit for this quantity type, specified
    by an arithmetic conversion (scaling and/or offset).

    A preferred unit is either a base unit or a derived unit selected
    for all units of one quantity type. The mandatory attribute "uom"
    shall reference the preferred unit that this conversion applies to.
    The conversion is specified by one of two alternative elements:
    "factor" or "formula".
    """

    factor_or_formula: float | FormulaType | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "factor",
                    "type": float,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "formula",
                    "type": FormulaType,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
