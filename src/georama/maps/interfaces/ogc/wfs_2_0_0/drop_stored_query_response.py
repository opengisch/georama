from dataclasses import dataclass

from georama.maps.interfaces.ogc.wfs_2_0_0.execution_status_type import (
    ExecutionStatusType,
)

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class DropStoredQueryResponse(ExecutionStatusType):
    class Meta:
        namespace = "http://www.opengis.net/wfs/2.0"
