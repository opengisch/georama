from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_id_type import AbstractIdType

__NAMESPACE__ = "http://www.opengis.net/ogc"


@dataclass
class FeatureIdType(AbstractIdType):
    fid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
