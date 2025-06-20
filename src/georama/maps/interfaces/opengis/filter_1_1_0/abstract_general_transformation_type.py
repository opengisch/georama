from dataclasses import dataclass, field
from typing import Any, Optional

from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    AbstractCoordinateOperationType,
    SourceCrs,
    TargetCrs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.operation_version import (
    OperationVersion,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralTransformationType(AbstractCoordinateOperationType):
    """An abstract operation on coordinates that usually includes a change of
    Datum.

    The parameters of a coordinate transformation are empirically derived from data containing the coordinates of a series of points in both coordinate reference systems. This computational process is usually "over-determined", allowing derivation of error (or accuracy) estimates for the transformation. Also, the stochastic nature of the parameters may result in multiple (different) versions of the same coordinate transformation.
    This abstract complexType is expected to be extended for well-known operation methods with many Transformation instances, in Application Schemas that define operation-method-specialized value element names and contents. This transformation uses an operation method with associated parameter values. However, operation methods and parameter values are directly associated with concrete subtypes, not with this abstract type. All concrete types derived from this type shall extend this type to include a "usesMethod" element that references one "OperationMethod" element. Similarly, all concrete types derived from this type shall extend this type to include one or more elements each named "uses...Value" that each use the type of an element substitutable for the "_generalParameterValue" element.

    :ivar description:
    :ivar group_name:
    :ivar parameter_name:
    :ivar method_name:
    :ivar ellipsoid_name:
    :ivar meridian_name:
    :ivar datum_name:
    :ivar cs_name:
    :ivar srs_name:
    :ivar name: Multiple names may be provided.  These will often be
        distinguished by being assigned by different authorities, as
        indicated by the value of the codeSpace attribute.  In an
        instance document there will usually only be one name per
        authority.
    :ivar operation_version:
    :ivar source_crs:
    :ivar target_crs:
    """

    description: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    group_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    parameter_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    method_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ellipsoid_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    meridian_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    datum_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    cs_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    srs_name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    name: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    operation_version: Optional[OperationVersion] = field(
        default=None,
        metadata={
            "name": "operationVersion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    source_crs: Optional[SourceCrs] = field(
        default=None,
        metadata={
            "name": "sourceCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    target_crs: Optional[TargetCrs] = field(
        default=None,
        metadata={
            "name": "targetCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
