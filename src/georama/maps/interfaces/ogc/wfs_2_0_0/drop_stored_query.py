from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.ogc.wfs_2_0_0.base_request_type import BaseRequestType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DropStoredQuery(BaseRequestType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
