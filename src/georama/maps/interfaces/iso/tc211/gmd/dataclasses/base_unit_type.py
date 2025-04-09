from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.reference_type import (
    ReferenceType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.unit_definition_type import (
    UnitDefinitionType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class BaseUnitType(UnitDefinitionType):
    units_system: Optional[ReferenceType] = field(
        default=None,
        metadata={
            "name": "unitsSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
