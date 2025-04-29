from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType
from georama.maps.interfaces.opengis.gml_3_2_1.modified_coordinate import (
    ModifiedCoordinate,
)
from georama.maps.interfaces.opengis.gml_3_2_1.sc_crs_property_type import (
    AbstractCoordinateOperationType,
    Conversion1,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.transformation import Transformation
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    transformation: Optional[Transformation] = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    conversion: Optional[Conversion1] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pass_through_operation: Optional["PassThroughOperation"] = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    type_value: TypeType = field(
        init=False,
        default=TypeType.SIMPLE,
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
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    nil_reason: Optional[str] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
        },
    )
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class CoordOperation(CoordinateOperationPropertyType):
    """
    Gml:coordOperation is an association role to a coordinate operation.
    """

    class Meta:
        name = "coordOperation"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesOperation(CoordinateOperationPropertyType):
    class Meta:
        name = "usesOperation"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesSingleOperation(CoordinateOperationPropertyType):
    class Meta:
        name = "usesSingleOperation"
        namespace = "http://www.opengis.net/gml/3.2"


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

    uses_operation: list[UsesOperation] = field(
        default_factory=list,
        metadata={
            "name": "usesOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_single_operation: list[UsesSingleOperation] = field(
        default_factory=list,
        metadata={
            "name": "usesSingleOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coord_operation: list[CoordOperation] = field(
        default_factory=list,
        metadata={
            "name": "coordOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
    modified_coordinate: list[ModifiedCoordinate] = field(
        default_factory=list,
        metadata={
            "name": "modifiedCoordinate",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    uses_operation: Optional[UsesOperation] = field(
        default=None,
        metadata={
            "name": "usesOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_single_operation: Optional[UsesSingleOperation] = field(
        default=None,
        metadata={
            "name": "usesSingleOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coord_operation: Optional[CoordOperation] = field(
        default=None,
        metadata={
            "name": "coordOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
        namespace = "http://www.opengis.net/gml/3.2"


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
        namespace = "http://www.opengis.net/gml/3.2"
