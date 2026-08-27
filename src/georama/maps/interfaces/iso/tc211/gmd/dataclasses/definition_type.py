from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_base_type import (
    DefinitionBaseType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.remarks import Remarks

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionType(DefinitionBaseType):
    remarks: Remarks | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
