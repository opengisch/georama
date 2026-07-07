from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.base_request_type import BaseRequestType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ListStoredQueriesType(BaseRequestType):
    pass
