from dataclasses import dataclass, field
from typing import Any, Optional, Union

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_general_parameter_value_property_type import (
    IncludesValue,
    ParameterValue2,
    UsesValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.abstract_object_type import (
    AbstractObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.affine_cs_2 import AffineCs2
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType
from georama.maps.interfaces.opengis.gml_3_2_1.anchor_definition import AnchorDefinition
from georama.maps.interfaces.opengis.gml_3_2_1.anchor_point import AnchorPoint
from georama.maps.interfaces.opengis.gml_3_2_1.cartesian_cs_2 import CartesianCs2
from georama.maps.interfaces.opengis.gml_3_2_1.character_string_property_type import (
    CharacterStringPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_operation_accuracy import (
    CoordinateOperationAccuracy,
)
from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_system import CoordinateSystem
from georama.maps.interfaces.opengis.gml_3_2_1.cylindrical_cs_2 import CylindricalCs2
from georama.maps.interfaces.opengis.gml_3_2_1.derived_crstype import DerivedCrstype
from georama.maps.interfaces.opengis.gml_3_2_1.ellipsoid_2 import Ellipsoid2
from georama.maps.interfaces.opengis.gml_3_2_1.ellipsoidal_cs_2 import EllipsoidalCs2
from georama.maps.interfaces.opengis.gml_3_2_1.ex_geographic_extent_property_type import (
    ExGeographicExtentPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ex_temporal_extent_property_type import (
    ExTemporalExtentPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.identified_object_type import (
    IdentifiedObjectType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.linear_cs_2 import LinearCs2
from georama.maps.interfaces.opengis.gml_3_2_1.method import Method
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.operation_version import OperationVersion
from georama.maps.interfaces.opengis.gml_3_2_1.origin import Origin
from georama.maps.interfaces.opengis.gml_3_2_1.pixel_in_cell import PixelInCell
from georama.maps.interfaces.opengis.gml_3_2_1.polar_cs_2 import PolarCs2
from georama.maps.interfaces.opengis.gml_3_2_1.prime_meridian_2 import PrimeMeridian2
from georama.maps.interfaces.opengis.gml_3_2_1.real_property_type import (
    RealPropertyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.realization_epoch import RealizationEpoch
from georama.maps.interfaces.opengis.gml_3_2_1.scope import Scope
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.spherical_cs_2 import SphericalCs2
from georama.maps.interfaces.opengis.gml_3_2_1.time_cs_2 import TimeCs2
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType
from georama.maps.interfaces.opengis.gml_3_2_1.user_defined_cs_2 import UserDefinedCs2
from georama.maps.interfaces.opengis.gml_3_2_1.uses_affine_cs import UsesAffineCs
from georama.maps.interfaces.opengis.gml_3_2_1.uses_cartesian_cs import UsesCartesianCs
from georama.maps.interfaces.opengis.gml_3_2_1.uses_cs import UsesCs
from georama.maps.interfaces.opengis.gml_3_2_1.uses_ellipsoid import UsesEllipsoid
from georama.maps.interfaces.opengis.gml_3_2_1.uses_ellipsoidal_cs import (
    UsesEllipsoidalCs,
)
from georama.maps.interfaces.opengis.gml_3_2_1.uses_method import UsesMethod
from georama.maps.interfaces.opengis.gml_3_2_1.uses_oblique_cartesian_cs import (
    UsesObliqueCartesianCs,
)
from georama.maps.interfaces.opengis.gml_3_2_1.uses_prime_meridian import (
    UsesPrimeMeridian,
)
from georama.maps.interfaces.opengis.gml_3_2_1.uses_spherical_cs import UsesSphericalCs
from georama.maps.interfaces.opengis.gml_3_2_1.uses_temporal_cs import UsesTemporalCs
from georama.maps.interfaces.opengis.gml_3_2_1.uses_time_cs import UsesTimeCs
from georama.maps.interfaces.opengis.gml_3_2_1.uses_vertical_cs import UsesVerticalCs
from georama.maps.interfaces.opengis.gml_3_2_1.vertical_cs_2 import VerticalCs2


@dataclass
class AbstractCrstype(IdentifiedObjectType):
    class Meta:
        name = "AbstractCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    domain_of_validity: list["DomainOfValidity"] = field(
        default_factory=list,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    scope: list[Scope] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )


@dataclass
class CrspropertyType:
    """
    Gml:CRSPropertyType is a property type for association roles to a CRS abstract
    coordinate reference system, either referencing or containing the definition of
    that CRS.
    """

    class Meta:
        name = "CRSPropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    compound_crs: Optional["CompoundCrs"] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geocentric_crs: Optional["GeocentricCrs"] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geographic_crs: Optional["GeographicCrs"] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_crs: Optional["TemporalCrs"] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    image_crs: Optional["ImageCrs"] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    engineering_crs: Optional["EngineeringCrs"] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_crs: Optional["VerticalCrs"] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodetic_crs: Optional["GeodeticCrs"] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derived_crs: Optional["DerivedCrs"] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    projected_crs: Optional["ProjectedCrs"] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class DomainOfValidity:
    """
    The gml:domainOfValidity property implements an association role to an
    EX_Extent object as encoded in ISO/TS 19139, either referencing or containing
    the definition of that extent.
    """

    class Meta:
        name = "domainOfValidity"
        namespace = "http://www.opengis.net/gml/3.2"

    ex_extent: Optional["ExExtent"] = field(
        default=None,
        metadata={
            "name": "EX_Extent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class AbstractDatumType(IdentifiedObjectType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    domain_of_validity: Optional[DomainOfValidity] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    scope: list[Scope] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    anchor_point: Optional[AnchorPoint] = field(
        default=None,
        metadata={
            "name": "anchorPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    anchor_definition: Optional[AnchorDefinition] = field(
        default=None,
        metadata={
            "name": "anchorDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    realization_epoch: Optional[RealizationEpoch] = field(
        default=None,
        metadata={
            "name": "realizationEpoch",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class SourceCrs(CrspropertyType):
    """
    Gml:sourceCRS is an association role to the source CRS (coordinate reference
    system) of this coordinate operation.
    """

    class Meta:
        name = "sourceCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TargetCrs(CrspropertyType):
    """
    Gml:targetCRS is an association role to the target CRS (coordinate reference
    system) of this coordinate operation.
    """

    class Meta:
        name = "targetCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractCoordinateOperationType(IdentifiedObjectType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    domain_of_validity: Optional[DomainOfValidity] = field(
        default=None,
        metadata={
            "name": "domainOfValidity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    scope: list[Scope] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    operation_version: Optional[OperationVersion] = field(
        default=None,
        metadata={
            "name": "operationVersion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinate_operation_accuracy: list[CoordinateOperationAccuracy] = field(
        default_factory=list,
        metadata={
            "name": "coordinateOperationAccuracy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    source_crs: Optional[SourceCrs] = field(
        default=None,
        metadata={
            "name": "sourceCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    target_crs: Optional[TargetCrs] = field(
        default=None,
        metadata={
            "name": "targetCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class EngineeringDatumType(AbstractDatumType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticDatumType(AbstractDatumType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    uses_prime_meridian: Optional[UsesPrimeMeridian] = field(
        default=None,
        metadata={
            "name": "usesPrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    prime_meridian: Optional[PrimeMeridian2] = field(
        default=None,
        metadata={
            "name": "primeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_ellipsoid: Optional[UsesEllipsoid] = field(
        default=None,
        metadata={
            "name": "usesEllipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ellipsoid: Optional[Ellipsoid2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class ImageDatumType(AbstractDatumType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    pixel_in_cell: Optional[PixelInCell] = field(
        default=None,
        metadata={
            "name": "pixelInCell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class TemporalDatumBaseType(AbstractDatumType):
    """The TemporalDatumBaseType partially defines the origin of a temporal
    coordinate reference system.

    This type restricts the AbstractDatumType to remove the
    "anchorDefinition" and "realizationEpoch" elements.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    anchor_point: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    anchor_definition: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    realization_epoch: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass
class VerticalDatumType(AbstractDatumType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralConversionType(AbstractCoordinateOperationType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

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


@dataclass
class EngineeringDatum1(EngineeringDatumType):
    """Gml:EngineeringDatum defines the origin of an engineering coordinate
    reference system, and is used in a region around that origin.

    This origin may be fixed with respect to the earth (such as a
    defined point at a construction site), or be a defined point on a
    moving vehicle (such as on a ship or satellite).
    """

    class Meta:
        name = "EngineeringDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticDatum1(GeodeticDatumType):
    """
    Gml:GeodeticDatum is a geodetic datum defines the precise location and
    orientation in 3-dimensional space of a defined ellipsoid (or sphere), or of a
    Cartesian coordinate system centered in this ellipsoid (or sphere).
    """

    class Meta:
        name = "GeodeticDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageDatum1(ImageDatumType):
    """Gml:ImageDatum defines the origin of an image coordinate reference system,
    and is used in a local context only.

    For an image datum, the anchor definition is usually either the
    centre of the image or the corner of the image. For more
    information, see ISO 19111 B.3.5.
    """

    class Meta:
        name = "ImageDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalDatumType(TemporalDatumBaseType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    origin: Optional[Origin] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class VerticalDatum1(VerticalDatumType):
    """
    Gml:VerticalDatum is a textual description and/or a set of parameters
    identifying a particular reference level surface used as a zero-height surface,
    including its position with respect to the Earth for any of the height types
    recognized by this International Standard.
    """

    class Meta:
        name = "VerticalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ConversionType(AbstractGeneralConversionType):
    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    uses_method: Optional[UsesMethod] = field(
        default=None,
        metadata={
            "name": "usesMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    method: Optional[Method] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    includes_value: list[IncludesValue] = field(
        default_factory=list,
        metadata={
            "name": "includesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_value: list[UsesValue] = field(
        default_factory=list,
        metadata={
            "name": "usesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    parameter_value: list[ParameterValue2] = field(
        default_factory=list,
        metadata={
            "name": "parameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class EngineeringDatumPropertyType:
    """
    Gml:EngineeringDatumPropertyType is a property type for association roles to an
    engineering datum, either referencing or containing the definition of that
    datum.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    engineering_datum: Optional[EngineeringDatum1] = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class GeodeticDatumPropertyType:
    """
    Gml:GeodeticDatumPropertyType is a property type for association roles to a
    geodetic datum, either referencing or containing the definition of that datum.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    geodetic_datum: Optional[GeodeticDatum1] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class ImageDatumPropertyType:
    """
    Gml:ImageDatumPropertyType is a property type for association roles to an image
    datum, either referencing or containing the definition of that datum.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    image_datum: Optional[ImageDatum1] = field(
        default=None,
        metadata={
            "name": "ImageDatum",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class TemporalDatum1(TemporalDatumType):
    """A gml:TemporalDatum defines the origin of a Temporal Reference System.

    This type omits the "anchorDefinition" and "realizationEpoch"
    elements and adds the "origin" element with the dateTime type.
    """

    class Meta:
        name = "TemporalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalDatumPropertyType:
    """
    Gml:VerticalDatumPropertyType is property type for association roles to a
    vertical datum, either referencing or containing the definition of that datum.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    vertical_datum: Optional[VerticalDatum1] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class Conversion1(ConversionType):
    """Gml:Conversion is a concrete operation on coordinates that does not include
    any change of Datum.

    The best-known example of a coordinate conversion is a map
    projection. The parameters describing coordinate conversions are
    defined rather than empirically derived. Note that some conversions
    have no parameters. This concrete complex type can be used without
    using a GML Application Schema that defines operation-method-
    specialized element names and contents, especially for methods with
    only one Conversion instance. The usesValue property elements are an
    unordered list of composition associations to the set of parameter
    values used by this conversion operation.
    """

    class Meta:
        name = "Conversion"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalDatumPropertyType:
    """
    Gml:TemporalDatumPropertyType is a property type for association roles to a
    temporal datum, either referencing or containing the definition of that datum.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    temporal_datum: Optional[TemporalDatum1] = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class EngineeringDatum2(EngineeringDatumPropertyType):
    """
    Gml:engineeringDatum is an association role to the engineering datum used by
    this CRS.
    """

    class Meta:
        name = "engineeringDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticDatum2(GeodeticDatumPropertyType):
    """
    Gml:geodeticDatum is an association role to the geodetic datum used by this
    CRS.
    """

    class Meta:
        name = "geodeticDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageDatum2(ImageDatumPropertyType):
    """
    Gml:imageDatum is an association role to the image datum used by this CRS.
    """

    class Meta:
        name = "imageDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesEngineeringDatum(EngineeringDatumPropertyType):
    class Meta:
        name = "usesEngineeringDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesGeodeticDatum(GeodeticDatumPropertyType):
    class Meta:
        name = "usesGeodeticDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesImageDatum(ImageDatumPropertyType):
    class Meta:
        name = "usesImageDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesVerticalDatum(VerticalDatumPropertyType):
    class Meta:
        name = "usesVerticalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class VerticalDatum2(VerticalDatumPropertyType):
    """
    Gml:verticalDatum is an association role to the vertical datum used by this
    CRS.
    """

    class Meta:
        name = "verticalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EngineeringCrstype(AbstractCrstype):
    class Meta:
        name = "EngineeringCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    uses_affine_cs: Optional[UsesAffineCs] = field(
        default=None,
        metadata={
            "name": "usesAffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    affine_cs: Optional[AffineCs2] = field(
        default=None,
        metadata={
            "name": "affineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cylindrical_cs: Optional[CylindricalCs2] = field(
        default=None,
        metadata={
            "name": "cylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    linear_cs: Optional[LinearCs2] = field(
        default=None,
        metadata={
            "name": "linearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polar_cs: Optional[PolarCs2] = field(
        default=None,
        metadata={
            "name": "polarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_spherical_cs: Optional[UsesSphericalCs] = field(
        default=None,
        metadata={
            "name": "usesSphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    spherical_cs: Optional[SphericalCs2] = field(
        default=None,
        metadata={
            "name": "sphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    user_defined_cs: Optional[UserDefinedCs2] = field(
        default=None,
        metadata={
            "name": "userDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_cs: Optional[UsesCs] = field(
        default=None,
        metadata={
            "name": "usesCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_engineering_datum: Optional[UsesEngineeringDatum] = field(
        default=None,
        metadata={
            "name": "usesEngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    engineering_datum: Optional[EngineeringDatum2] = field(
        default=None,
        metadata={
            "name": "engineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class GeneralConversionPropertyType:
    """
    Gml:GeneralConversionPropertyType is a property type for association roles to a
    general conversion, either referencing or containing the definition of that
    conversion.
    """

    class Meta:
        target_namespace = "http://www.opengis.net/gml/3.2"

    conversion: Optional[Conversion1] = field(
        default=None,
        metadata={
            "name": "Conversion",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class GeocentricCrstype(AbstractCrstype):
    class Meta:
        name = "GeocentricCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_spherical_cs: Optional[UsesSphericalCs] = field(
        default=None,
        metadata={
            "name": "usesSphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class GeodeticCrstype(AbstractCrstype):
    """
    Gml:GeodeticCRS is a coordinate reference system based on a geodetic datum.
    """

    class Meta:
        name = "GeodeticCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    uses_ellipsoidal_cs: Optional[UsesEllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "usesEllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ellipsoidal_cs: Optional[EllipsoidalCs2] = field(
        default=None,
        metadata={
            "name": "ellipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_spherical_cs: Optional[UsesSphericalCs] = field(
        default=None,
        metadata={
            "name": "usesSphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    spherical_cs: Optional[SphericalCs2] = field(
        default=None,
        metadata={
            "name": "sphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodetic_datum: Optional[GeodeticDatum2] = field(
        default=None,
        metadata={
            "name": "geodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class GeographicCrstype(AbstractCrstype):
    class Meta:
        name = "GeographicCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    uses_ellipsoidal_cs: Optional[UsesEllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "usesEllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    uses_geodetic_datum: Optional[UsesGeodeticDatum] = field(
        default=None,
        metadata={
            "name": "usesGeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )


@dataclass
class ImageCrstype(AbstractCrstype):
    class Meta:
        name = "ImageCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_affine_cs: Optional[UsesAffineCs] = field(
        default=None,
        metadata={
            "name": "usesAffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    affine_cs: Optional[AffineCs2] = field(
        default=None,
        metadata={
            "name": "affineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_oblique_cartesian_cs: Optional[UsesObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_image_datum: Optional[UsesImageDatum] = field(
        default=None,
        metadata={
            "name": "usesImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    image_datum: Optional[ImageDatum2] = field(
        default=None,
        metadata={
            "name": "imageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class VerticalCrstype(AbstractCrstype):
    class Meta:
        name = "VerticalCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    uses_vertical_cs: Optional[UsesVerticalCs] = field(
        default=None,
        metadata={
            "name": "usesVerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_cs: Optional[VerticalCs2] = field(
        default=None,
        metadata={
            "name": "verticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_vertical_datum: Optional[UsesVerticalDatum] = field(
        default=None,
        metadata={
            "name": "usesVerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_datum: Optional[VerticalDatum2] = field(
        default=None,
        metadata={
            "name": "verticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class TemporalDatum2(TemporalDatumPropertyType):
    """
    Gml:temporalDatum is an association role to the temporal datum used by this
    CRS.
    """

    class Meta:
        name = "temporalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesTemporalDatum(TemporalDatumPropertyType):
    class Meta:
        name = "usesTemporalDatum"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EngineeringCrs(EngineeringCrstype):
    """Gml:EngineeringCRS is a contextually local coordinate reference system which
    can be divided into two broad categories:

    -       earth-fixed systems applied to engineering activities on or near the surface of the earth;
    -       CRSs on moving platforms such as road vehicles, vessels, aircraft, or spacecraft, see ISO 19111 8.3.
    """

    class Meta:
        name = "EngineeringCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeocentricCrs(GeocentricCrstype):
    class Meta:
        name = "GeocentricCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeodeticCrs(GeodeticCrstype):
    class Meta:
        name = "GeodeticCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class GeographicCrs(GeographicCrstype):
    class Meta:
        name = "GeographicCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ImageCrs(ImageCrstype):
    """Gml:ImageCRS is an engineering coordinate reference system applied to
    locations in images.

    Image coordinate reference systems are treated as a separate sub-
    type because the definition of the associated image datum contains
    two attributes not relevant to other engineering datums.
    """

    class Meta:
        name = "ImageCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TemporalCrstype(AbstractCrstype):
    class Meta:
        name = "TemporalCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    uses_time_cs: Optional[UsesTimeCs] = field(
        default=None,
        metadata={
            "name": "usesTimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_cs: Optional[TimeCs2] = field(
        default=None,
        metadata={
            "name": "timeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_temporal_cs: Optional[UsesTemporalCs] = field(
        default=None,
        metadata={
            "name": "usesTemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_temporal_datum: Optional[UsesTemporalDatum] = field(
        default=None,
        metadata={
            "name": "usesTemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_datum: Optional[TemporalDatum2] = field(
        default=None,
        metadata={
            "name": "temporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class VerticalCrs(VerticalCrstype):
    """Gml:VerticalCRS is a 1D coordinate reference system used for recording
    heights or depths.

    Vertical CRSs make use of the direction of gravity to define the
    concept of height or depth, but the relationship with gravity may
    not be straightforward. By implication, ellipsoidal heights (h)
    cannot be captured in a vertical coordinate reference system.
    Ellipsoidal heights cannot exist independently, but only as an
    inseparable part of a 3D coordinate tuple defined in a geographic 3D
    coordinate reference system.
    """

    class Meta:
        name = "VerticalCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Conversion2(GeneralConversionPropertyType):
    """
    Gml:conversion is an association role to the coordinate conversion used to
    define the derived CRS.
    """

    class Meta:
        name = "conversion"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DefinedByConversion(GeneralConversionPropertyType):
    class Meta:
        name = "definedByConversion"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralDerivedCrstype(AbstractCrstype):
    class Meta:
        name = "AbstractGeneralDerivedCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    defined_by_conversion: Optional[DefinedByConversion] = field(
        default=None,
        metadata={
            "name": "definedByConversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    conversion: Optional[Conversion2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class GeodeticCrspropertyType:
    """
    Gml:GeodeticCRSPropertyType is a property type for association roles to a
    geodetic coordinate reference system, either referencing or containing the
    definition of that reference system.
    """

    class Meta:
        name = "GeodeticCRSPropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class GeographicCrspropertyType:
    class Meta:
        name = "GeographicCRSPropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class TemporalCrs(TemporalCrstype):
    """
    Gml:TemporalCRS is a 1D coordinate reference system used for the recording of
    time.
    """

    class Meta:
        name = "TemporalCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BaseGeodeticCrs(GeodeticCrspropertyType):
    """
    Gml:baseGeodeticCRS is an association role to the geodetic coordinate reference
    system used by this projected CRS.
    """

    class Meta:
        name = "baseGeodeticCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class BaseGeographicCrs(GeographicCrspropertyType):
    class Meta:
        name = "baseGeographicCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ProjectedCrstype(AbstractGeneralDerivedCrstype):
    class Meta:
        name = "ProjectedCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    base_geodetic_crs: Optional[BaseGeodeticCrs] = field(
        default=None,
        metadata={
            "name": "baseGeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    base_geographic_crs: Optional[BaseGeographicCrs] = field(
        default=None,
        metadata={
            "name": "baseGeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_cartesian_cs: Optional[UsesCartesianCs] = field(
        default=None,
        metadata={
            "name": "usesCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cartesian_cs: Optional[CartesianCs2] = field(
        default=None,
        metadata={
            "name": "cartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class ProjectedCrs(ProjectedCrstype):
    """Gml:ProjectedCRS is a 2D coordinate reference system used to approximate the
    shape of the earth on a planar surface, but in such a way that the distortion
    that is inherent to the approximation is carefully controlled and known.

    Distortion correction is commonly applied to calculated bearings and
    distances to produce values that are a close match to actual field
    values.
    """

    class Meta:
        name = "ProjectedCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SingleCrspropertyType:
    """
    Gml:SingleCRSPropertyType is a property type for association roles to a single
    coordinate reference system, either referencing or containing the definition of
    that coordinate reference system.
    """

    class Meta:
        name = "SingleCRSPropertyType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derived_crs: Optional["DerivedCrs"] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
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
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class BaseCrs(SingleCrspropertyType):
    """
    Gml:baseCRS is an association role to the coordinate reference system used by
    this derived CRS.
    """

    class Meta:
        name = "baseCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ComponentReferenceSystem(SingleCrspropertyType):
    """The gml:componentReferenceSystem elements are an ordered sequence of
    associations to all the component coordinate reference systems included in this
    compound coordinate reference system.

    The gml:AggregationAttributeGroup should be used to specify that the
    gml:componentReferenceSystem properties are ordered.
    """

    class Meta:
        name = "componentReferenceSystem"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class IncludesSingleCrs(SingleCrspropertyType):
    class Meta:
        name = "includesSingleCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class CompoundCrstype(AbstractCrstype):
    class Meta:
        name = "CompoundCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    includes_single_crs: list[IncludesSingleCrs] = field(
        default_factory=list,
        metadata={
            "name": "includesSingleCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    component_reference_system: list[ComponentReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "componentReferenceSystem",
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
class DerivedCrstype1(AbstractGeneralDerivedCrstype):
    class Meta:
        name = "DerivedCRSType"
        target_namespace = "http://www.opengis.net/gml/3.2"

    base_crs: Optional[BaseCrs] = field(
        default=None,
        metadata={
            "name": "baseCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    derived_crstype: Optional[DerivedCrstype] = field(
        default=None,
        metadata={
            "name": "derivedCRSType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    uses_cs: Optional[UsesCs] = field(
        default=None,
        metadata={
            "name": "usesCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinate_system: Optional[CoordinateSystem] = field(
        default=None,
        metadata={
            "name": "coordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class CompoundCrs(CompoundCrstype):
    """Gml:CompundCRS is a coordinate reference system describing the position of
    points through two or more independent coordinate reference systems.

    It is associated with a non-repeating sequence of two or more
    instances of SingleCRS.
    """

    class Meta:
        name = "CompoundCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DerivedCrs(DerivedCrstype1):
    """Gml:DerivedCRS is a single coordinate reference system that is defined by
    its coordinate conversion from another single coordinate reference system known
    as the base CRS.

    The base CRS can be a projected coordinate reference system, if this
    DerivedCRS is used for a georectified grid coverage as described in
    ISO 19123, Clause 8.
    """

    class Meta:
        name = "DerivedCRS"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ScCrsPropertyType:
    class Meta:
        name = "SC_CRS_PropertyType"
        target_namespace = "http://www.isotc211.org/2005/gsr"

    compound_crs: Optional[CompoundCrs] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )


@dataclass
class ExVerticalExtentType(AbstractObjectType):
    """
    Vertical domain of dataset.
    """

    class Meta:
        name = "EX_VerticalExtent_Type"
        target_namespace = "http://www.isotc211.org/2005/gmd"

    minimum_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "minimumValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    maximum_value: Optional[RealPropertyType] = field(
        default=None,
        metadata={
            "name": "maximumValue",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )
    vertical_crs: Optional[ScCrsPropertyType] = field(
        default=None,
        metadata={
            "name": "verticalCRS",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
            "required": True,
        },
    )


@dataclass
class ExVerticalExtent(ExVerticalExtentType):
    class Meta:
        name = "EX_VerticalExtent"
        namespace = "http://www.isotc211.org/2005/gmd"


@dataclass
class ExVerticalExtentPropertyType:
    class Meta:
        name = "EX_VerticalExtent_PropertyType"
        target_namespace = "http://www.isotc211.org/2005/gmd"

    ex_vertical_extent: Optional[ExVerticalExtent] = field(
        default=None,
        metadata={
            "name": "EX_VerticalExtent",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
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
    uuidref: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "namespace": "http://www.isotc211.org/2005/gco",
            "pattern": r"other:\w{2,}",
        },
    )


@dataclass
class ExExtentType(AbstractObjectType):
    """
    Information about spatial, vertical, and temporal extent.
    """

    class Meta:
        name = "EX_Extent_Type"
        target_namespace = "http://www.isotc211.org/2005/gmd"

    description: Optional[CharacterStringPropertyType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    geographic_element: list[ExGeographicExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "geographicElement",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    temporal_element: list[ExTemporalExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "temporalElement",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )
    vertical_element: list[ExVerticalExtentPropertyType] = field(
        default_factory=list,
        metadata={
            "name": "verticalElement",
            "type": "Element",
            "namespace": "http://www.isotc211.org/2005/gmd",
        },
    )


@dataclass
class ExExtent(ExExtentType):
    class Meta:
        name = "EX_Extent"
        namespace = "http://www.isotc211.org/2005/gmd"
