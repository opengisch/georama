from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gmltype import (
    AbstractGmltype,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.identifier import Identifier

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DefinitionBaseType(AbstractGmltype):
    identifier: Optional[Identifier] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
