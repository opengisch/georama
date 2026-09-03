from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.reference_type import ReferenceType
from georama.maps.interfaces.opengis.gml_3_2_1.unit_definition_type import (
    UnitDefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class BaseUnitType(UnitDefinitionType):
    units_system: ReferenceType | None = field(
        default=None,
        metadata={
            "name": "unitsSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
