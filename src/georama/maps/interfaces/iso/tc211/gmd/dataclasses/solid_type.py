from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_solid_type import (
    AbstractSolidType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.shell_property_type import (
    ShellPropertyType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SolidType(AbstractSolidType):
    exterior: ShellPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    interior: list[ShellPropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
