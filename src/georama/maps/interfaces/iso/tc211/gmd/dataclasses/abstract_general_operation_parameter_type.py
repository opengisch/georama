from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.identified_object_type import (
    IdentifiedObjectType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.minimum_occurs import (
    MinimumOccurs,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameterType(IdentifiedObjectType):
    minimum_occurs: Optional[MinimumOccurs] = field(
        default=None,
        metadata={
            "name": "minimumOccurs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
