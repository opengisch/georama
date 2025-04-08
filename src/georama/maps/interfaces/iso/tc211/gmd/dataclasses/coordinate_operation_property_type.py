from dataclasses import dataclass, field
from typing import List, Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.aggregation_type import (
    AggregationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.modified_coordinate import (
    ModifiedCoordinate,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    AbstractCoordinateOperationType,
    Conversion1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.transformation import (
    Transformation,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationPropertyType:
    """
    Gml:CoordinateOperationPropertyType is a property type for association roles to
    a coordinate operation, either referencing or containing the definition of that
    coordinate operation.
    """

    concatenated_operation: Optional["ConcatenatedOperation"] = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pass_through_operation: Optional["PassThroughOperation"] = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conversion: Optional[Conversion1] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    type_value: str = field(
        init=False,
        default="simple",
        metadata={
            "name": "type",
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    href: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class CoordOperation(CoordinateOperationPropertyType):
    """
    Gml:coordOperation is an association role to a coordinate operation.
    """

    class Meta:
        name = "coordOperation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesOperation(CoordinateOperationPropertyType):
    """
    Gml:usesOperation is deprecated, gml:coordOperation shall be used instead.
    """

    class Meta:
        name = "usesOperation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesSingleOperation(CoordinateOperationPropertyType):
    class Meta:
        name = "usesSingleOperation"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ConcatenatedOperationType(AbstractCoordinateOperationType):
    """Gml:ConcatenatedOperation is an ordered sequence of two or more coordinate
    operations.

    This sequence of operations is constrained by the requirement that
    the source coordinate reference system of step (n+1) must be the
    same as the target coordinate reference system of step (n). The
    source coordinate reference system of the first step and the target
    coordinate reference system of the last step are the source and
    target coordinate reference system associated with the concatenated
    operation. Instead of a forward operation, an inverse operation may
    be used for one or more of the operation steps mentioned above, if
    the inverse operation is uniquely defined by the forward operation.
    The gml:coordOperation property elements are an ordered sequence of
    associations to the two or more operations used by this concatenated
    operation. The AggregationAttributeGroup should be used to specify
    that the coordOperation associations are ordered.
    """

    uses_operation: List[UsesOperation] = field(
        default_factory=list,
        metadata={
            "name": "usesOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    uses_single_operation: List[UsesSingleOperation] = field(
        default_factory=list,
        metadata={
            "name": "usesSingleOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coord_operation: List[CoordOperation] = field(
        default_factory=list,
        metadata={
            "name": "coordOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class PassThroughOperationType(AbstractCoordinateOperationType):
    modified_coordinate: List[ModifiedCoordinate] = field(
        default_factory=list,
        metadata={
            "name": "modifiedCoordinate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 1,
        },
    )
    uses_operation: Optional[UsesOperation] = field(
        default=None,
        metadata={
            "name": "usesOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    uses_single_operation: Optional[UsesSingleOperation] = field(
        default=None,
        metadata={
            "name": "usesSingleOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coord_operation: Optional[CoordOperation] = field(
        default=None,
        metadata={
            "name": "coordOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    aggregation_type: Optional[AggregationType] = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class ConcatenatedOperation(ConcatenatedOperationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class PassThroughOperation(PassThroughOperationType):
    """Gml:PassThroughOperation is a pass-through operation specifies that a subset
    of a coordinate tuple is subject to a specific coordinate operation.

    The modifiedCoordinate property elements are an ordered sequence of
    positive integers defining the positions in a coordinate tuple of
    the coordinates affected by this pass-through operation. The
    AggregationAttributeGroup should be used to specify that the
    modifiedCoordinate elements are ordered.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
