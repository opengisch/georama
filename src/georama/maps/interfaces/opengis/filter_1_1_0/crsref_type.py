from dataclasses import dataclass, field
from typing import Any, ForwardRef, Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.absolute_external_positional_accuracy import (
    AbsoluteExternalPositionalAccuracy,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_coordinate_operation_base_type import (
    AbstractCoordinateOperationBaseType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_reference_system_type import (
    AbstractReferenceSystemType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_operation_id import (
    CoordinateOperationId,
)
from georama.maps.interfaces.opengis.filter_1_1_0.covariance_matrix import (
    CovarianceMatrix,
)
from georama.maps.interfaces.opengis.filter_1_1_0.derived_crstype import DerivedCrstype
from georama.maps.interfaces.opengis.filter_1_1_0.engineering_crs import EngineeringCrs
from georama.maps.interfaces.opengis.filter_1_1_0.geocentric_crs import GeocentricCrs
from georama.maps.interfaces.opengis.filter_1_1_0.geographic_crs import GeographicCrs
from georama.maps.interfaces.opengis.filter_1_1_0.image_crs import ImageCrs
from georama.maps.interfaces.opengis.filter_1_1_0.operation_version import (
    OperationVersion,
)
from georama.maps.interfaces.opengis.filter_1_1_0.relative_internal_positional_accuracy import (
    RelativeInternalPositionalAccuracy,
)
from georama.maps.interfaces.opengis.filter_1_1_0.remarks import Remarks
from georama.maps.interfaces.opengis.filter_1_1_0.scope import Scope
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.temporal_crs import TemporalCrs
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType
from georama.maps.interfaces.opengis.filter_1_1_0.uses_cartesian_cs import (
    UsesCartesianCs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.uses_cs import UsesCs
from georama.maps.interfaces.opengis.filter_1_1_0.uses_method import UsesMethod
from georama.maps.interfaces.opengis.filter_1_1_0.uses_value import UsesValue
from georama.maps.interfaces.opengis.filter_1_1_0.valid_area import ValidArea
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_crs import VerticalCrs

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CrsrefType:
    """
    Association to a CRS abstract coordinate reference system, either referencing
    or containing the definition of that CRS.
    """

    class Meta:
        name = "CRSRefType"

    choice: Optional[
        Union[
            "CompoundCrs",
            TemporalCrs,
            ImageCrs,
            EngineeringCrs,
            "DerivedCrs",
            "ProjectedCrs",
            GeocentricCrs,
            VerticalCrs,
            GeographicCrs,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundCRS",
                    "type": ForwardRef("CompoundCrs"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalCRS",
                    "type": TemporalCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ImageCRS",
                    "type": ImageCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EngineeringCRS",
                    "type": EngineeringCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DerivedCRS",
                    "type": ForwardRef("DerivedCrs"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ProjectedCRS",
                    "type": ForwardRef("ProjectedCrs"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeocentricCRS",
                    "type": GeocentricCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalCRS",
                    "type": VerticalCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeographicCRS",
                    "type": GeographicCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class CoordinateReferenceSystemRefType:
    """
    Association to a coordinate reference system, either referencing or containing
    the definition of that reference system.
    """

    choice: Optional[
        Union[
            TemporalCrs,
            ImageCrs,
            EngineeringCrs,
            "DerivedCrs",
            "ProjectedCrs",
            GeocentricCrs,
            VerticalCrs,
            GeographicCrs,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TemporalCRS",
                    "type": TemporalCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ImageCRS",
                    "type": ImageCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EngineeringCRS",
                    "type": EngineeringCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DerivedCRS",
                    "type": ForwardRef("DerivedCrs"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ProjectedCRS",
                    "type": ForwardRef("ProjectedCrs"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeocentricCRS",
                    "type": GeocentricCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalCRS",
                    "type": VerticalCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeographicCRS",
                    "type": GeographicCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class BaseCrs(CoordinateReferenceSystemRefType):
    """
    Association to the coordinate reference system used by this derived CRS.
    """

    class Meta:
        name = "baseCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class IncludesCrs(CoordinateReferenceSystemRefType):
    """
    An association to a component coordinate reference system included in this
    compound coordinate reference system.
    """

    class Meta:
        name = "includesCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SourceCrs(CrsrefType):
    """
    Association to the source CRS (coordinate reference system) of this coordinate
    operation.
    """

    class Meta:
        name = "sourceCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class TargetCrs(CrsrefType):
    """Association to the target CRS (coordinate reference system) of this
    coordinate operation.

    For constraints on multiplicity of "sourceCRS" and "targetCRS", see
    UML model of Coordinate Operation package in OGC Abstract
    Specification topic 2.
    """

    class Meta:
        name = "targetCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractCoordinateOperationType(AbstractCoordinateOperationBaseType):
    """A mathematical operation on coordinates that transforms or converts
    coordinates to another coordinate reference system.

    Many but not all coordinate operations (from CRS A to CRS B) also
    uniquely define the inverse operation (from CRS B to CRS A). In some
    cases, the operation method algorithm for the inverse operation is
    the same as for the forward algorithm, but the signs of some
    operation parameter values must be reversed. In other cases,
    different algorithms are required for the forward and inverse
    operations, but the same operation parameter values are used. If
    (some) entirely different parameter values are needed, a different
    coordinate operation shall be defined.

    :ivar coordinate_operation_id: Set of alternative identifications of
        this coordinate operation. The first coordinateOperationID, if
        any, is normally the primary identification code, and any others
        are aliases.
    :ivar remarks: Comments on or information about this coordinate
        operation, including source information.
    :ivar operation_version:
    :ivar valid_area:
    :ivar scope:
    :ivar
        covariance_matrix_or_relative_internal_positional_accuracy_or_absolute_external_positional_accuracy:
    :ivar source_crs:
    :ivar target_crs:
    """

    coordinate_operation_id: list[CoordinateOperationId] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_version: Optional[OperationVersion] = field(
        default=None,
        metadata={
            "name": "operationVersion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    valid_area: Optional[ValidArea] = field(
        default=None,
        metadata={
            "name": "validArea",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    scope: Optional[Scope] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    covariance_matrix_or_relative_internal_positional_accuracy_or_absolute_external_positional_accuracy: list[
        Union[
            CovarianceMatrix,
            RelativeInternalPositionalAccuracy,
            AbsoluteExternalPositionalAccuracy,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "covarianceMatrix",
                    "type": CovarianceMatrix,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "relativeInternalPositionalAccuracy",
                    "type": RelativeInternalPositionalAccuracy,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "absoluteExternalPositionalAccuracy",
                    "type": AbsoluteExternalPositionalAccuracy,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    source_crs: Optional[SourceCrs] = field(
        default=None,
        metadata={
            "name": "sourceCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    target_crs: Optional[TargetCrs] = field(
        default=None,
        metadata={
            "name": "targetCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class CompoundCrstype(AbstractReferenceSystemType):
    """
    A coordinate reference system describing the position of points through two or
    more independent coordinate reference systems.

    :ivar includes_crs: Ordered sequence of associations to all the
        component coordinate reference systems included in this compound
        coordinate reference system.
    """

    class Meta:
        name = "CompoundCRSType"

    includes_crs: list[IncludesCrs] = field(
        default_factory=list,
        metadata={
            "name": "includesCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        },
    )


@dataclass
class AbstractGeneralConversionType(AbstractCoordinateOperationType):
    """An abstract operation on coordinates that does not include any change of
    datum.

    The best-known example of a coordinate conversion is a map projection. The parameters describing coordinate conversions are defined rather than empirically derived. Note that some conversions have no parameters.
    This abstract complexType is expected to be extended for well-known operation methods with many Conversion instances, in Application Schemas that define operation-method-specialized element names and contents. This conversion uses an operation method, usually with associated parameter values. However, operation methods and parameter values are directly associated with concrete subtypes, not with this abstract type. All concrete types derived from this type shall extend this type to include a "usesMethod" element that references the "OperationMethod" element. Similarly, all concrete types derived from this type shall extend this type to include zero or more elements each named "uses...Value" that each use the type of an element substitutable for the "_generalParameterValue" element.
    """

    operation_version: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    source_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    target_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    description: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class CompoundCrs(CompoundCrstype):
    class Meta:
        name = "CompoundCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ConversionType(AbstractGeneralConversionType):
    """A concrete operation on coordinates that does not include any change of
    Datum.

    The best-known example of a coordinate conversion is a map
    projection. The parameters describing coordinate conversions are
    defined rather than empirically derived. Note that some conversions
    have no parameters. This concrete complexType can be used with all
    operation methods, without using an Application Schema that defines
    operation-method-specialized element names and contents, especially
    for methods with only one Conversion instance.

    :ivar uses_method:
    :ivar uses_value: Unordered list of composition associations to the
        set of parameter values used by this conversion operation.
    """

    uses_method: Optional[UsesMethod] = field(
        default=None,
        metadata={
            "name": "usesMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    uses_value: list[UsesValue] = field(
        default_factory=list,
        metadata={
            "name": "usesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class Conversion(ConversionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class GeneralConversionRefType:
    """
    Association to a general conversion, either referencing or containing the
    definition of that conversion.
    """

    conversion: Optional[Conversion] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    remote_schema: Optional[str] = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class DefinedByConversion(GeneralConversionRefType):
    """
    Association to the coordinate conversion used to define this derived CRS.
    """

    class Meta:
        name = "definedByConversion"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralDerivedCrstype(AbstractReferenceSystemType):
    """A coordinate reference system that is defined by its coordinate conversion
    from another coordinate reference system (not by a datum).

    This abstract complexType shall not be used, extended, or
    restricted, in an Application Schema, to define a concrete subtype
    with a meaning equivalent to a concrete subtype specified in this
    document.
    """

    class Meta:
        name = "AbstractGeneralDerivedCRSType"

    base_crs: Optional[BaseCrs] = field(
        default=None,
        metadata={
            "name": "baseCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    defined_by_conversion: Optional[DefinedByConversion] = field(
        default=None,
        metadata={
            "name": "definedByConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class DerivedCrstype1(AbstractGeneralDerivedCrstype):
    """A coordinate reference system that is defined by its coordinate conversion
    from another coordinate reference system but is not a projected coordinate
    reference system.

    This category includes coordinate reference systems derived from a
    projected coordinate reference system.
    """

    class Meta:
        name = "DerivedCRSType"

    derived_crstype: Optional[DerivedCrstype] = field(
        default=None,
        metadata={
            "name": "derivedCRSType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    uses_cs: Optional[UsesCs] = field(
        default=None,
        metadata={
            "name": "usesCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class ProjectedCrstype(AbstractGeneralDerivedCrstype):
    """A 2D coordinate reference system used to approximate the shape of the earth
    on a planar surface, but in such a way that the distortion that is inherent to
    the approximation is carefully controlled and known.

    Distortion correction is commonly applied to calculated bearings and
    distances to produce values that are a close match to actual field
    values.
    """

    class Meta:
        name = "ProjectedCRSType"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class DerivedCrs(DerivedCrstype1):
    class Meta:
        name = "DerivedCRS"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ProjectedCrs(ProjectedCrstype):
    class Meta:
        name = "ProjectedCRS"
        namespace = "http://www.opengis.net/gml"
