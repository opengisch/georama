from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gmltype import (
    AbstractGmltype,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.identifier import Identifier

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionBaseType(AbstractGmltype):
    identifier: Identifier | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
