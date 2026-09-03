from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_crstype import (
    AbstractCoordinateOperationType,
    SourceCrs,
    TargetCrs,
)
from georama.maps.interfaces.opengis.gml_3_2_1.operation_version import OperationVersion

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralTransformationType(AbstractCoordinateOperationType):
    operation_version: OperationVersion | None = field(
        default=None,
        metadata={
            "name": "operationVersion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    source_crs: SourceCrs | None = field(
        default=None,
        metadata={
            "name": "sourceCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    target_crs: TargetCrs | None = field(
        default=None,
        metadata={
            "name": "targetCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
