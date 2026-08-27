from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_version import (
    OperationVersion,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    AbstractCoordinateOperationType,
    SourceCrs,
    TargetCrs,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralTransformationType(AbstractCoordinateOperationType):
    operation_version: OperationVersion | None = field(
        default=None,
        metadata={
            "name": "operationVersion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    source_crs: SourceCrs | None = field(
        default=None,
        metadata={
            "name": "sourceCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    target_crs: TargetCrs | None = field(
        default=None,
        metadata={
            "name": "targetCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
