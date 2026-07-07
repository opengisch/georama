from dataclasses import dataclass, field
from typing import Any, ForwardRef, Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_feature_type import (
    AbstractFeatureType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_operation_parameter_ref_type import (
    OperationParameterGroup,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_gmltype import (
    AbstractGmltype,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_time_primitive_type import (
    TimeEdge,
    TimeInstant,
    TimeNode,
    TimePeriod,
)
from georama.maps.interfaces.opengis.filter_1_1_0.abstract_topo_primitive_type import (
    Edge,
    Face,
    Node,
    TopoSolid,
)
from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.base_unit import BaseUnit
from georama.maps.interfaces.opengis.filter_1_1_0.boolean import Boolean
from georama.maps.interfaces.opengis.filter_1_1_0.boolean_list import BooleanList
from georama.maps.interfaces.opengis.filter_1_1_0.cartesian_cs import CartesianCs
from georama.maps.interfaces.opengis.filter_1_1_0.category import Category
from georama.maps.interfaces.opengis.filter_1_1_0.category_extent import CategoryExtent
from georama.maps.interfaces.opengis.filter_1_1_0.category_list import CategoryList
from georama.maps.interfaces.opengis.filter_1_1_0.composite_solid_type import (
    CompositeSolid,
)
from georama.maps.interfaces.opengis.filter_1_1_0.concatenated_operation import (
    ConcatenatedOperation,
)
from georama.maps.interfaces.opengis.filter_1_1_0.conventional_unit import (
    ConventionalUnit,
)
from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_system_axis import (
    CoordinateSystemAxis,
)
from georama.maps.interfaces.opengis.filter_1_1_0.count import Count
from georama.maps.interfaces.opengis.filter_1_1_0.count_extent import CountExtent
from georama.maps.interfaces.opengis.filter_1_1_0.count_list import CountList
from georama.maps.interfaces.opengis.filter_1_1_0.coverage_function import (
    CoverageFunction,
)
from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    CompoundCrs,
    Conversion,
    DerivedCrs,
    ProjectedCrs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.curve_property_type import (
    CompositeCurve,
    Curve,
    OrientableCurve,
)
from georama.maps.interfaces.opengis.filter_1_1_0.cylindrical_cs import CylindricalCs
from georama.maps.interfaces.opengis.filter_1_1_0.definition import Definition
from georama.maps.interfaces.opengis.filter_1_1_0.definition_proxy import (
    DefinitionProxy,
)
from georama.maps.interfaces.opengis.filter_1_1_0.derived_unit import DerivedUnit
from georama.maps.interfaces.opengis.filter_1_1_0.dictionary_type import (
    DefinitionCollection,
    Dictionary,
)
from georama.maps.interfaces.opengis.filter_1_1_0.direction import Direction
from georama.maps.interfaces.opengis.filter_1_1_0.domain_set import DomainSet
from georama.maps.interfaces.opengis.filter_1_1_0.double_or_null_tuple_list import (
    DoubleOrNullTupleList,
)
from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoid import Ellipsoid
from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoidal_cs import EllipsoidalCs
from georama.maps.interfaces.opengis.filter_1_1_0.engineering_crs import EngineeringCrs
from georama.maps.interfaces.opengis.filter_1_1_0.engineering_datum import (
    EngineeringDatum,
)
from georama.maps.interfaces.opengis.filter_1_1_0.feature_style_1 import FeatureStyle1
from georama.maps.interfaces.opengis.filter_1_1_0.file_value_model_type import (
    FileValueModelType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.generic_meta_data import (
    GenericMetaData,
)
from georama.maps.interfaces.opengis.filter_1_1_0.geocentric_crs import GeocentricCrs
from georama.maps.interfaces.opengis.filter_1_1_0.geodetic_datum import GeodeticDatum
from georama.maps.interfaces.opengis.filter_1_1_0.geographic_crs import GeographicCrs
from georama.maps.interfaces.opengis.filter_1_1_0.geometric_complex import (
    GeometricComplex,
)
from georama.maps.interfaces.opengis.filter_1_1_0.geometry_array_property_type import (
    MultiGeometry,
)
from georama.maps.interfaces.opengis.filter_1_1_0.geometry_style_1 import GeometryStyle1
from georama.maps.interfaces.opengis.filter_1_1_0.graph_style_1 import GraphStyle1
from georama.maps.interfaces.opengis.filter_1_1_0.grid import Grid
from georama.maps.interfaces.opengis.filter_1_1_0.grid_domain import GridDomain
from georama.maps.interfaces.opengis.filter_1_1_0.image_crs import ImageCrs
from georama.maps.interfaces.opengis.filter_1_1_0.image_datum import ImageDatum
from georama.maps.interfaces.opengis.filter_1_1_0.label_style_1 import LabelStyle1
from georama.maps.interfaces.opengis.filter_1_1_0.line_string import LineString
from georama.maps.interfaces.opengis.filter_1_1_0.linear_cs import LinearCs
from georama.maps.interfaces.opengis.filter_1_1_0.linear_ring import LinearRing
from georama.maps.interfaces.opengis.filter_1_1_0.measure_type import MeasureType
from georama.maps.interfaces.opengis.filter_1_1_0.moving_object_status import (
    MovingObjectStatus,
)
from georama.maps.interfaces.opengis.filter_1_1_0.multi_curve import MultiCurve
from georama.maps.interfaces.opengis.filter_1_1_0.multi_curve_domain import (
    MultiCurveDomain,
)
from georama.maps.interfaces.opengis.filter_1_1_0.multi_line_string import (
    MultiLineString,
)
from georama.maps.interfaces.opengis.filter_1_1_0.multi_point import MultiPoint
from georama.maps.interfaces.opengis.filter_1_1_0.multi_point_domain import (
    MultiPointDomain,
)
from georama.maps.interfaces.opengis.filter_1_1_0.multi_polygon import MultiPolygon
from georama.maps.interfaces.opengis.filter_1_1_0.multi_solid import MultiSolid
from georama.maps.interfaces.opengis.filter_1_1_0.multi_solid_domain import (
    MultiSolidDomain,
)
from georama.maps.interfaces.opengis.filter_1_1_0.multi_surface import MultiSurface
from georama.maps.interfaces.opengis.filter_1_1_0.multi_surface_domain import (
    MultiSurfaceDomain,
)
from georama.maps.interfaces.opengis.filter_1_1_0.null import Null
from georama.maps.interfaces.opengis.filter_1_1_0.oblique_cartesian_cs import (
    ObliqueCartesianCs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.operation_method import (
    OperationMethod,
)
from georama.maps.interfaces.opengis.filter_1_1_0.operation_parameter import (
    OperationParameter,
)
from georama.maps.interfaces.opengis.filter_1_1_0.pass_through_operation import (
    PassThroughOperation,
)
from georama.maps.interfaces.opengis.filter_1_1_0.point import Point
from georama.maps.interfaces.opengis.filter_1_1_0.polar_cs import PolarCs
from georama.maps.interfaces.opengis.filter_1_1_0.polygon import Polygon
from georama.maps.interfaces.opengis.filter_1_1_0.polyhedral_surface import (
    PolyhedralSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.prime_meridian import PrimeMeridian
from georama.maps.interfaces.opengis.filter_1_1_0.quantity import Quantity
from georama.maps.interfaces.opengis.filter_1_1_0.quantity_extent import QuantityExtent
from georama.maps.interfaces.opengis.filter_1_1_0.quantity_list import QuantityList
from georama.maps.interfaces.opengis.filter_1_1_0.rectified_grid import RectifiedGrid
from georama.maps.interfaces.opengis.filter_1_1_0.rectified_grid_domain import (
    RectifiedGridDomain,
)
from georama.maps.interfaces.opengis.filter_1_1_0.ring import Ring
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.solid import Solid
from georama.maps.interfaces.opengis.filter_1_1_0.spherical_cs import SphericalCs
from georama.maps.interfaces.opengis.filter_1_1_0.style import Style
from georama.maps.interfaces.opengis.filter_1_1_0.surface import Surface
from georama.maps.interfaces.opengis.filter_1_1_0.surface_property_type import (
    CompositeSurface,
    OrientableSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.temporal_crs import TemporalCrs
from georama.maps.interfaces.opengis.filter_1_1_0.temporal_cs import TemporalCs
from georama.maps.interfaces.opengis.filter_1_1_0.temporal_datum import TemporalDatum
from georama.maps.interfaces.opengis.filter_1_1_0.time_calendar import TimeCalendar
from georama.maps.interfaces.opengis.filter_1_1_0.time_calendar_era import (
    TimeCalendarEra,
)
from georama.maps.interfaces.opengis.filter_1_1_0.time_clock import TimeClock
from georama.maps.interfaces.opengis.filter_1_1_0.time_coordinate_system import (
    TimeCoordinateSystem,
)
from georama.maps.interfaces.opengis.filter_1_1_0.time_ordinal_reference_system import (
    TimeOrdinalReferenceSystem,
)
from georama.maps.interfaces.opengis.filter_1_1_0.time_topology_complex import (
    TimeTopologyComplex,
)
from georama.maps.interfaces.opengis.filter_1_1_0.tin import Tin
from georama.maps.interfaces.opengis.filter_1_1_0.topo_complex_type import TopoComplex
from georama.maps.interfaces.opengis.filter_1_1_0.topology_style_1 import TopologyStyle1
from georama.maps.interfaces.opengis.filter_1_1_0.transformation import Transformation
from georama.maps.interfaces.opengis.filter_1_1_0.triangulated_surface import (
    TriangulatedSurface,
)
from georama.maps.interfaces.opengis.filter_1_1_0.tuple_list import TupleList
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType
from georama.maps.interfaces.opengis.filter_1_1_0.unit_definition import UnitDefinition
from georama.maps.interfaces.opengis.filter_1_1_0.user_defined_cs import UserDefinedCs
from georama.maps.interfaces.opengis.filter_1_1_0.valid_time import ValidTime
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_crs import VerticalCrs
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_cs import VerticalCs
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_datum import VerticalDatum

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class FeatureArrayPropertyType:
    """Container for features - follow gml:ArrayAssociationType pattern."""

    choice: list[
        Union[
            "DirectedObservationAtDistance",
            "DirectedObservation",
            "Observation",
            "RectifiedGridCoverage",
            "GridCoverage",
            "MultiSolidCoverage",
            "MultiSurfaceCoverage",
            "MultiCurveCoverage",
            "MultiPointCoverage",
            "FeatureCollection",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DirectedObservationAtDistance",
                    "type": ForwardRef("DirectedObservationAtDistance"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservation",
                    "type": ForwardRef("DirectedObservation"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Observation",
                    "type": ForwardRef("Observation"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGridCoverage",
                    "type": ForwardRef("RectifiedGridCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GridCoverage",
                    "type": ForwardRef("GridCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolidCoverage",
                    "type": ForwardRef("MultiSolidCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurfaceCoverage",
                    "type": ForwardRef("MultiSurfaceCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurveCoverage",
                    "type": ForwardRef("MultiCurveCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPointCoverage",
                    "type": ForwardRef("MultiPointCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureCollection",
                    "type": ForwardRef("FeatureCollection"),
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )


@dataclass
class ArrayType(AbstractGmltype):
    """A non-abstract generic collection type that can be used as a document element for a homogeneous collection of any GML types - Geometries, Topologies, Features ..."""

    members: Optional["Members"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class BagType(AbstractGmltype):
    """A non-abstract generic collection type that can be used as a document element for a collection of any GML types - Geometries, Topologies, Features ...
    FeatureCollections may only contain Features.  GeometryCollections may only contain Geometrys.  Bags are less constrained  they must contain objects that are substitutable for gml:_Object.  This may mix several levels, including Features, Definitions, Dictionaries, Geometries etc.
    The content model would ideally be
    member 0..*
    members 0..1
    member 0..*
    for maximum flexibility in building a collection from both homogeneous and distinct components:
    included "member" elements each contain a single Object
    an included "members" element contains a set of Objects
    However, this is non-deterministic, thus prohibited by XSD."""

    member: list["Member"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    members: Optional["Members"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class CompositeValueType(AbstractGmltype):
    """Aggregate value built from other Values using the Composite pattern.

    It contains zero or an arbitrary number of valueComponent elements,
    and zero or one valueComponents elements.  It may be used for
    strongly coupled aggregates (vectors, tensors) or for arbitrary
    collections of values.
    """

    value_component: list["ValueComponent"] = field(
        default_factory=list,
        metadata={
            "name": "valueComponent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_components: Optional["ValueComponents"] = field(
        default=None,
        metadata={
            "name": "valueComponents",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class FeaturePropertyType:
    """Container for a feature - follow gml:AssociationType pattern."""

    choice: Optional[
        Union[
            "DirectedObservationAtDistance",
            "DirectedObservation",
            "Observation",
            "RectifiedGridCoverage",
            "GridCoverage",
            "MultiSolidCoverage",
            "MultiSurfaceCoverage",
            "MultiCurveCoverage",
            "MultiPointCoverage",
            "FeatureCollection",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DirectedObservationAtDistance",
                    "type": ForwardRef("DirectedObservationAtDistance"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservation",
                    "type": ForwardRef("DirectedObservation"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Observation",
                    "type": ForwardRef("Observation"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGridCoverage",
                    "type": ForwardRef("RectifiedGridCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GridCoverage",
                    "type": ForwardRef("GridCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolidCoverage",
                    "type": ForwardRef("MultiSolidCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurfaceCoverage",
                    "type": ForwardRef("MultiSurfaceCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurveCoverage",
                    "type": ForwardRef("MultiCurveCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPointCoverage",
                    "type": ForwardRef("MultiPointCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureCollection",
                    "type": ForwardRef("FeatureCollection"),
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
class FeatureMembers(FeatureArrayPropertyType):
    class Meta:
        name = "featureMembers"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Array(ArrayType):
    """
    Generic GML element to contain a homogeneous array of GML _Objects.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Bag(BagType):
    """
    Generic GML element to contain a heterogeneous collection of GML _Objects.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class CompositeValue(CompositeValueType):
    """
    Aggregate value built using the Composite pattern.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ValueArrayType(CompositeValueType):
    """A Value Array is used for homogeneous arrays of primitive and aggregate
    values.

    The member values may be scalars, composites, arrays or lists.
    ValueArray has the same content model as CompositeValue, but the
    member values must be homogeneous.  The element declaration contains
    a Schematron constraint which expresses this restriction precisely.
    Since the members are homogeneous, the referenceSystem (uom,
    codeSpace) may be specified on the ValueArray itself and implicitly
    inherited by all the members if desired.    Note that
    a_ScalarValueList is preferred for arrays of Scalar Values since
    this is a more efficient encoding.
    """

    code_space: Optional[str] = field(
        default=None,
        metadata={
            "name": "codeSpace",
            "type": "Attribute",
        },
    )
    uom: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class FeatureMember(FeaturePropertyType):
    class Meta:
        name = "featureMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Using(FeaturePropertyType):
    """
    This element contains or points to a description of a sensor, instrument or
    procedure used for the observation.
    """

    class Meta:
        name = "using"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractFeatureCollectionType(AbstractFeatureType):
    """
    A feature collection contains zero or more features.
    """

    feature_member: list[FeatureMember] = field(
        default_factory=list,
        metadata={
            "name": "featureMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_members: Optional[FeatureMembers] = field(
        default=None,
        metadata={
            "name": "featureMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class AssociationType:
    """A pattern or base for derived types used to specify complex types corresponding to an  unspecified UML association - either composition or aggregation.  Restricts the cardinality of Objects contained in the association to a maximum of one.  An instance of this type can contain an element representing an Object, or serve as a pointer to a remote Object.
    Descendents of this type can be restricted in an application schema to
    * allow only specified classes as valid participants in the aggregation
    * allow only association by reference (i.e. empty the content model) or by value (i.e. remove the xlinks).
    When used for association by reference, the value of the gml:remoteSchema attribute can be used to locate a schema fragment that constrains the target instance.
    In many cases it is desirable to impose the constraint prohibiting the occurence of both reference and value in the same instance, as that would be ambiguous.  This is accomplished by adding a directive in the annotation element of the element declaration.  This directive can be in the form of normative prose, or can use a Schematron pattern to automatically constrain co-occurrence - see the declaration for _strictAssociation below.
    If co-occurence is not prohibited, then both a link and content may be present.  If this occurs in an instance, then the rule for interpretation is that the instance found by traversing the href provides the normative value of the property, and should be used when possible.  The value(s) included as content may be used if the remote instance cannot be resolved.  This may be considered to be a "cached" version of the value(s).
    """

    choice: Optional[
        Union[
            GenericMetaData,
            GraphStyle1,
            LabelStyle1,
            TopologyStyle1,
            GeometryStyle1,
            FeatureStyle1,
            Style,
            TopoComplex,
            TopoSolid,
            Face,
            Edge,
            Node,
            MovingObjectStatus,
            "DirectedObservationAtDistance",
            "DirectedObservation",
            "Observation",
            "RectifiedGridCoverage",
            "GridCoverage",
            "MultiSolidCoverage",
            "MultiSurfaceCoverage",
            "MultiCurveCoverage",
            "MultiPointCoverage",
            "FeatureCollection",
            TimeTopologyComplex,
            TimeEdge,
            TimeNode,
            TimePeriod,
            TimeInstant,
            MultiLineString,
            MultiPolygon,
            MultiSolid,
            MultiSurface,
            MultiCurve,
            MultiPoint,
            MultiGeometry,
            RectifiedGrid,
            Grid,
            GeometricComplex,
            Ring,
            LinearRing,
            Solid,
            CompositeSolid,
            OrientableSurface,
            Tin,
            TriangulatedSurface,
            PolyhedralSurface,
            Surface,
            CompositeSurface,
            Polygon,
            OrientableCurve,
            Curve,
            CompositeCurve,
            LineString,
            Point,
            TimeCalendarEra,
            TimeClock,
            TimeCalendar,
            TimeOrdinalReferenceSystem,
            TimeCoordinateSystem,
            OperationParameterGroup,
            OperationParameter,
            OperationMethod,
            Transformation,
            Conversion,
            PassThroughOperation,
            ConcatenatedOperation,
            Ellipsoid,
            PrimeMeridian,
            GeodeticDatum,
            TemporalDatum,
            VerticalDatum,
            ImageDatum,
            EngineeringDatum,
            ObliqueCartesianCs,
            CylindricalCs,
            PolarCs,
            SphericalCs,
            UserDefinedCs,
            LinearCs,
            TemporalCs,
            VerticalCs,
            CartesianCs,
            EllipsoidalCs,
            CoordinateSystemAxis,
            CompoundCrs,
            TemporalCrs,
            ImageCrs,
            EngineeringCrs,
            DerivedCrs,
            ProjectedCrs,
            GeocentricCrs,
            VerticalCrs,
            GeographicCrs,
            ConventionalUnit,
            DerivedUnit,
            BaseUnit,
            UnitDefinition,
            DefinitionProxy,
            DefinitionCollection,
            Dictionary,
            Definition,
            Array,
            Bag,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GenericMetaData",
                    "type": GenericMetaData,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GraphStyle",
                    "type": GraphStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LabelStyle",
                    "type": LabelStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopologyStyle",
                    "type": TopologyStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeometryStyle",
                    "type": GeometryStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureStyle",
                    "type": FeatureStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Style",
                    "type": Style,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopoComplex",
                    "type": TopoComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopoSolid",
                    "type": TopoSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Face",
                    "type": Face,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Edge",
                    "type": Edge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Node",
                    "type": Node,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MovingObjectStatus",
                    "type": MovingObjectStatus,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservationAtDistance",
                    "type": ForwardRef("DirectedObservationAtDistance"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservation",
                    "type": ForwardRef("DirectedObservation"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Observation",
                    "type": ForwardRef("Observation"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGridCoverage",
                    "type": ForwardRef("RectifiedGridCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GridCoverage",
                    "type": ForwardRef("GridCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolidCoverage",
                    "type": ForwardRef("MultiSolidCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurfaceCoverage",
                    "type": ForwardRef("MultiSurfaceCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurveCoverage",
                    "type": ForwardRef("MultiCurveCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPointCoverage",
                    "type": ForwardRef("MultiPointCoverage"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureCollection",
                    "type": ForwardRef("FeatureCollection"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeTopologyComplex",
                    "type": TimeTopologyComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeEdge",
                    "type": TimeEdge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeNode",
                    "type": TimeNode,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimePeriod",
                    "type": TimePeriod,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeInstant",
                    "type": TimeInstant,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiLineString",
                    "type": MultiLineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPolygon",
                    "type": MultiPolygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolid",
                    "type": MultiSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurface",
                    "type": MultiSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurve",
                    "type": MultiCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPoint",
                    "type": MultiPoint,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiGeometry",
                    "type": MultiGeometry,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGrid",
                    "type": RectifiedGrid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Grid",
                    "type": Grid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeometricComplex",
                    "type": GeometricComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Ring",
                    "type": Ring,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearRing",
                    "type": LinearRing,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Solid",
                    "type": Solid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSolid",
                    "type": CompositeSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableSurface",
                    "type": OrientableSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Tin",
                    "type": Tin,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TriangulatedSurface",
                    "type": TriangulatedSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolyhedralSurface",
                    "type": PolyhedralSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Surface",
                    "type": Surface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSurface",
                    "type": CompositeSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Polygon",
                    "type": Polygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableCurve",
                    "type": OrientableCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Curve",
                    "type": Curve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeCurve",
                    "type": CompositeCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Point",
                    "type": Point,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCalendarEra",
                    "type": TimeCalendarEra,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeClock",
                    "type": TimeClock,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCalendar",
                    "type": TimeCalendar,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeOrdinalReferenceSystem",
                    "type": TimeOrdinalReferenceSystem,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCoordinateSystem",
                    "type": TimeCoordinateSystem,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationParameterGroup",
                    "type": OperationParameterGroup,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationParameter",
                    "type": OperationParameter,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationMethod",
                    "type": OperationMethod,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Transformation",
                    "type": Transformation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Conversion",
                    "type": Conversion,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PassThroughOperation",
                    "type": PassThroughOperation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ConcatenatedOperation",
                    "type": ConcatenatedOperation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Ellipsoid",
                    "type": Ellipsoid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PrimeMeridian",
                    "type": PrimeMeridian,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeodeticDatum",
                    "type": GeodeticDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalDatum",
                    "type": TemporalDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalDatum",
                    "type": VerticalDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ImageDatum",
                    "type": ImageDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EngineeringDatum",
                    "type": EngineeringDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ObliqueCartesianCS",
                    "type": ObliqueCartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CylindricalCS",
                    "type": CylindricalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolarCS",
                    "type": PolarCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "SphericalCS",
                    "type": SphericalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "UserDefinedCS",
                    "type": UserDefinedCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearCS",
                    "type": LinearCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalCS",
                    "type": TemporalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalCS",
                    "type": VerticalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CartesianCS",
                    "type": CartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EllipsoidalCS",
                    "type": EllipsoidalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CoordinateSystemAxis",
                    "type": CoordinateSystemAxis,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompoundCRS",
                    "type": CompoundCrs,
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
                    "type": DerivedCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ProjectedCRS",
                    "type": ProjectedCrs,
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
                {
                    "name": "ConventionalUnit",
                    "type": ConventionalUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DerivedUnit",
                    "type": DerivedUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "BaseUnit",
                    "type": BaseUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "UnitDefinition",
                    "type": UnitDefinition,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DefinitionProxy",
                    "type": DefinitionProxy,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DefinitionCollection",
                    "type": DefinitionCollection,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Dictionary",
                    "type": Dictionary,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Definition",
                    "type": Definition,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Array",
                    "type": Array,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Bag",
                    "type": Bag,
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
class ValueArray(ValueArrayType):
    """A Value Array is used for homogeneous arrays of primitive and aggregate
    values.

    _ScalarValueList is preferred for arrays of Scalar Values since this
    is more efficient.  Since "choice" is not available for attribute
    groups, an external constraint (e.g. Schematron) would be required
    to enforce the selection of only one of these through schema
    validation
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeatureCollectionType(AbstractFeatureCollectionType):
    """
    Concrete generic feature collection.
    """


@dataclass
class RangeParametersType:
    """Metadata about the rangeSet.

    Definition of record structure. This is required if the rangeSet is
    encoded in a DataBlock. We use a gml:_Value with empty values as a
    map of the composite value structure.
    """

    choice: Optional[
        Union[
            Boolean,
            Category,
            Quantity,
            Count,
            BooleanList,
            CategoryList,
            QuantityList,
            CountList,
            CategoryExtent,
            QuantityExtent,
            CountExtent,
            ValueArray,
            CompositeValue,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Boolean",
                    "type": Boolean,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Category",
                    "type": Category,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Quantity",
                    "type": Quantity,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Count",
                    "type": Count,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "BooleanList",
                    "type": BooleanList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CategoryList",
                    "type": CategoryList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "QuantityList",
                    "type": QuantityList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CountList",
                    "type": CountList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CategoryExtent",
                    "type": CategoryExtent,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "QuantityExtent",
                    "type": QuantityExtent,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CountExtent",
                    "type": CountExtent,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ValueArray",
                    "type": ValueArray,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeValue",
                    "type": CompositeValue,
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
class Member(AssociationType):
    class Meta:
        name = "member"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ResultOf(AssociationType):
    """The result of the observation: an image, external object, etc"""

    class Meta:
        name = "resultOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeatureCollection(FeatureCollectionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class RangeParameters(RangeParametersType):
    class Meta:
        name = "rangeParameters"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DataBlockType:
    range_parameters: Optional[RangeParameters] = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    tuple_list_or_double_or_null_tuple_list: Optional[
        Union[TupleList, DoubleOrNullTupleList]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "tupleList",
                    "type": TupleList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "doubleOrNullTupleList",
                    "type": DoubleOrNullTupleList,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )


@dataclass
class FileType:
    range_parameters: Optional[RangeParameters] = field(
        default=None,
        metadata={
            "name": "rangeParameters",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "fileName",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    file_structure: Optional[FileValueModelType] = field(
        default=None,
        metadata={
            "name": "fileStructure",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    mime_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "mimeType",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    compression: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class DataBlock(DataBlockType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class File(FileType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class RangeSetType:
    choice: list[
        Union[
            ValueArray,
            BooleanList,
            CategoryList,
            QuantityList,
            CountList,
            DataBlock,
            File,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ValueArray",
                    "type": ValueArray,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "BooleanList",
                    "type": BooleanList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CategoryList",
                    "type": CategoryList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "QuantityList",
                    "type": QuantityList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CountList",
                    "type": CountList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DataBlock",
                    "type": DataBlock,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "File",
                    "type": File,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )


@dataclass
class RangeSet(RangeSetType):
    class Meta:
        name = "rangeSet"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractCoverageType(AbstractFeatureType):
    """Abstract element which acts as the head of a substitution group for
    coverages.

    Note that a coverage is a GML feature.
    """

    choice_1: Optional[
        Union[
            RectifiedGridDomain,
            GridDomain,
            MultiSolidDomain,
            MultiSurfaceDomain,
            MultiCurveDomain,
            MultiPointDomain,
            DomainSet,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "rectifiedGridDomain",
                    "type": RectifiedGridDomain,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "gridDomain",
                    "type": GridDomain,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "multiSolidDomain",
                    "type": MultiSolidDomain,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "multiSurfaceDomain",
                    "type": MultiSurfaceDomain,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "multiCurveDomain",
                    "type": MultiCurveDomain,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "multiPointDomain",
                    "type": MultiPointDomain,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "domainSet",
                    "type": DomainSet,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    range_set: Optional[RangeSet] = field(
        default=None,
        metadata={
            "name": "rangeSet",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    dimension: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class AbstractDiscreteCoverageType(AbstractCoverageType):
    """A discrete coverage consists of a domain set, range set and optionally a
    coverage function.

    The domain set consists of either geometry or temporal objects,
    finite in number. The range set is comprised of a finite number of
    attribute values each of which is associated to every direct
    position within any single spatiotemporal object in the domain. In
    other words, the range values are constant on each spatiotemporal
    object in the domain. This coverage function maps each element from
    the coverage domain to an element in its range. This definition
    conforms to ISO 19123.
    """

    coverage_function: Optional[CoverageFunction] = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class GridCoverageType(AbstractDiscreteCoverageType):
    choice_2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location_or_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    grid_domain: Optional[GridDomain] = field(
        default=None,
        metadata={
            "name": "gridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class MultiCurveCoverageType(AbstractDiscreteCoverageType):
    """
    A discrete coverage type whose domain is defined by a collection of curves.
    """

    choice_2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location_or_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve_domain: Optional[MultiCurveDomain] = field(
        default=None,
        metadata={
            "name": "multiCurveDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class MultiPointCoverageType(AbstractDiscreteCoverageType):
    """
    A discrete coverage type whose domain is defined by a collection of point.
    """

    choice_2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location_or_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_point_domain: Optional[MultiPointDomain] = field(
        default=None,
        metadata={
            "name": "multiPointDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class MultiSolidCoverageType(AbstractDiscreteCoverageType):
    """
    A discrete coverage type whose domain is defined by a collection of Solids.
    """

    choice_2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location_or_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid_domain: Optional[MultiSolidDomain] = field(
        default=None,
        metadata={
            "name": "multiSolidDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class MultiSurfaceCoverageType(AbstractDiscreteCoverageType):
    """
    A discrete coverage type whose domain is defined by a collection of surface
    patches (includes polygons, triangles, rectangles, etc).
    """

    choice_2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location_or_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_surface_domain: Optional[MultiSurfaceDomain] = field(
        default=None,
        metadata={
            "name": "multiSurfaceDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class RectifiedGridCoverageType(AbstractDiscreteCoverageType):
    choice_2: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location_or_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    rectified_grid_domain: Optional[RectifiedGridDomain] = field(
        default=None,
        metadata={
            "name": "rectifiedGridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class GridCoverage(GridCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiCurveCoverage(MultiCurveCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiPointCoverage(MultiPointCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiSolidCoverage(MultiSolidCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class MultiSurfaceCoverage(MultiSurfaceCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class RectifiedGridCoverage(RectifiedGridCoverageType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TargetPropertyType:
    """
    Container for an object representing the target or subject of an observation.
    """

    choice: Optional[
        Union[
            "DirectedObservationAtDistance",
            "DirectedObservation",
            "Observation",
            RectifiedGridCoverage,
            GridCoverage,
            MultiSolidCoverage,
            MultiSurfaceCoverage,
            MultiCurveCoverage,
            MultiPointCoverage,
            FeatureCollection,
            MultiLineString,
            MultiPolygon,
            MultiSolid,
            MultiSurface,
            MultiCurve,
            MultiPoint,
            MultiGeometry,
            RectifiedGrid,
            Grid,
            GeometricComplex,
            Ring,
            LinearRing,
            Solid,
            CompositeSolid,
            OrientableSurface,
            Tin,
            TriangulatedSurface,
            PolyhedralSurface,
            Surface,
            CompositeSurface,
            Polygon,
            OrientableCurve,
            Curve,
            CompositeCurve,
            LineString,
            Point,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DirectedObservationAtDistance",
                    "type": ForwardRef("DirectedObservationAtDistance"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservation",
                    "type": ForwardRef("DirectedObservation"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Observation",
                    "type": ForwardRef("Observation"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGridCoverage",
                    "type": RectifiedGridCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GridCoverage",
                    "type": GridCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolidCoverage",
                    "type": MultiSolidCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurfaceCoverage",
                    "type": MultiSurfaceCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurveCoverage",
                    "type": MultiCurveCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPointCoverage",
                    "type": MultiPointCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureCollection",
                    "type": FeatureCollection,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiLineString",
                    "type": MultiLineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPolygon",
                    "type": MultiPolygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolid",
                    "type": MultiSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurface",
                    "type": MultiSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurve",
                    "type": MultiCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPoint",
                    "type": MultiPoint,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiGeometry",
                    "type": MultiGeometry,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGrid",
                    "type": RectifiedGrid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Grid",
                    "type": Grid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeometricComplex",
                    "type": GeometricComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Ring",
                    "type": Ring,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearRing",
                    "type": LinearRing,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Solid",
                    "type": Solid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSolid",
                    "type": CompositeSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableSurface",
                    "type": OrientableSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Tin",
                    "type": Tin,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TriangulatedSurface",
                    "type": TriangulatedSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolyhedralSurface",
                    "type": PolyhedralSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Surface",
                    "type": Surface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSurface",
                    "type": CompositeSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Polygon",
                    "type": Polygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableCurve",
                    "type": OrientableCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Curve",
                    "type": Curve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeCurve",
                    "type": CompositeCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Point",
                    "type": Point,
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
class Subject(TargetPropertyType):
    """Synonym for target - common word used for photographs"""

    class Meta:
        name = "subject"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Target(TargetPropertyType):
    """
    This element contains or points to the specimen, region or station which is the
    object of the observation.
    """

    class Meta:
        name = "target"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ObservationType(AbstractFeatureType):
    valid_time: Optional[ValidTime] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    using: Optional[Using] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    subject_or_target: Optional[Union[Subject, Target]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "subject",
                    "type": Subject,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "target",
                    "type": Target,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )
    result_of: Optional[ResultOf] = field(
        default=None,
        metadata={
            "name": "resultOf",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class DirectedObservationType(ObservationType):
    direction: Optional[Direction] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class Observation(ObservationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class DirectedObservation(DirectedObservationType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class DirectedObservationAtDistanceType(DirectedObservationType):
    distance: Optional[MeasureType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )


@dataclass
class DirectedObservationAtDistance(DirectedObservationAtDistanceType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ArrayAssociationType:
    """A base for derived types used to specify complex types containing an array of objects, by unspecified UML association - either composition or aggregation.  An instance of this type contains elements representing Objects.
    Ideally this type would be derived by extension of AssociationType.
    However, this leads to a non-deterministic content model, since both the base and the extension have minOccurs="0", and is thus prohibited in XML Schema.
    """

    choice: list[
        Union[
            GenericMetaData,
            GraphStyle1,
            LabelStyle1,
            TopologyStyle1,
            GeometryStyle1,
            FeatureStyle1,
            Style,
            TopoComplex,
            TopoSolid,
            Face,
            Edge,
            Node,
            MovingObjectStatus,
            DirectedObservationAtDistance,
            DirectedObservation,
            Observation,
            RectifiedGridCoverage,
            GridCoverage,
            MultiSolidCoverage,
            MultiSurfaceCoverage,
            MultiCurveCoverage,
            MultiPointCoverage,
            FeatureCollection,
            TimeTopologyComplex,
            TimeEdge,
            TimeNode,
            TimePeriod,
            TimeInstant,
            MultiLineString,
            MultiPolygon,
            MultiSolid,
            MultiSurface,
            MultiCurve,
            MultiPoint,
            MultiGeometry,
            RectifiedGrid,
            Grid,
            GeometricComplex,
            Ring,
            LinearRing,
            Solid,
            CompositeSolid,
            OrientableSurface,
            Tin,
            TriangulatedSurface,
            PolyhedralSurface,
            Surface,
            CompositeSurface,
            Polygon,
            OrientableCurve,
            Curve,
            CompositeCurve,
            LineString,
            Point,
            TimeCalendarEra,
            TimeClock,
            TimeCalendar,
            TimeOrdinalReferenceSystem,
            TimeCoordinateSystem,
            OperationParameterGroup,
            OperationParameter,
            OperationMethod,
            Transformation,
            Conversion,
            PassThroughOperation,
            ConcatenatedOperation,
            Ellipsoid,
            PrimeMeridian,
            GeodeticDatum,
            TemporalDatum,
            VerticalDatum,
            ImageDatum,
            EngineeringDatum,
            ObliqueCartesianCs,
            CylindricalCs,
            PolarCs,
            SphericalCs,
            UserDefinedCs,
            LinearCs,
            TemporalCs,
            VerticalCs,
            CartesianCs,
            EllipsoidalCs,
            CoordinateSystemAxis,
            CompoundCrs,
            TemporalCrs,
            ImageCrs,
            EngineeringCrs,
            DerivedCrs,
            ProjectedCrs,
            GeocentricCrs,
            VerticalCrs,
            GeographicCrs,
            ConventionalUnit,
            DerivedUnit,
            BaseUnit,
            UnitDefinition,
            DefinitionProxy,
            DefinitionCollection,
            Dictionary,
            Definition,
            Array,
            Bag,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GenericMetaData",
                    "type": GenericMetaData,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GraphStyle",
                    "type": GraphStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LabelStyle",
                    "type": LabelStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopologyStyle",
                    "type": TopologyStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeometryStyle",
                    "type": GeometryStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureStyle",
                    "type": FeatureStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Style",
                    "type": Style,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopoComplex",
                    "type": TopoComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopoSolid",
                    "type": TopoSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Face",
                    "type": Face,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Edge",
                    "type": Edge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Node",
                    "type": Node,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MovingObjectStatus",
                    "type": MovingObjectStatus,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservationAtDistance",
                    "type": DirectedObservationAtDistance,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservation",
                    "type": DirectedObservation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Observation",
                    "type": Observation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGridCoverage",
                    "type": RectifiedGridCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GridCoverage",
                    "type": GridCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolidCoverage",
                    "type": MultiSolidCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurfaceCoverage",
                    "type": MultiSurfaceCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurveCoverage",
                    "type": MultiCurveCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPointCoverage",
                    "type": MultiPointCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureCollection",
                    "type": FeatureCollection,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeTopologyComplex",
                    "type": TimeTopologyComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeEdge",
                    "type": TimeEdge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeNode",
                    "type": TimeNode,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimePeriod",
                    "type": TimePeriod,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeInstant",
                    "type": TimeInstant,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiLineString",
                    "type": MultiLineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPolygon",
                    "type": MultiPolygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolid",
                    "type": MultiSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurface",
                    "type": MultiSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurve",
                    "type": MultiCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPoint",
                    "type": MultiPoint,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiGeometry",
                    "type": MultiGeometry,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGrid",
                    "type": RectifiedGrid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Grid",
                    "type": Grid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeometricComplex",
                    "type": GeometricComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Ring",
                    "type": Ring,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearRing",
                    "type": LinearRing,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Solid",
                    "type": Solid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSolid",
                    "type": CompositeSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableSurface",
                    "type": OrientableSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Tin",
                    "type": Tin,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TriangulatedSurface",
                    "type": TriangulatedSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolyhedralSurface",
                    "type": PolyhedralSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Surface",
                    "type": Surface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSurface",
                    "type": CompositeSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Polygon",
                    "type": Polygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableCurve",
                    "type": OrientableCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Curve",
                    "type": Curve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeCurve",
                    "type": CompositeCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Point",
                    "type": Point,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCalendarEra",
                    "type": TimeCalendarEra,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeClock",
                    "type": TimeClock,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCalendar",
                    "type": TimeCalendar,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeOrdinalReferenceSystem",
                    "type": TimeOrdinalReferenceSystem,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCoordinateSystem",
                    "type": TimeCoordinateSystem,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationParameterGroup",
                    "type": OperationParameterGroup,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationParameter",
                    "type": OperationParameter,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationMethod",
                    "type": OperationMethod,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Transformation",
                    "type": Transformation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Conversion",
                    "type": Conversion,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PassThroughOperation",
                    "type": PassThroughOperation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ConcatenatedOperation",
                    "type": ConcatenatedOperation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Ellipsoid",
                    "type": Ellipsoid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PrimeMeridian",
                    "type": PrimeMeridian,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeodeticDatum",
                    "type": GeodeticDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalDatum",
                    "type": TemporalDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalDatum",
                    "type": VerticalDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ImageDatum",
                    "type": ImageDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EngineeringDatum",
                    "type": EngineeringDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ObliqueCartesianCS",
                    "type": ObliqueCartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CylindricalCS",
                    "type": CylindricalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolarCS",
                    "type": PolarCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "SphericalCS",
                    "type": SphericalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "UserDefinedCS",
                    "type": UserDefinedCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearCS",
                    "type": LinearCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalCS",
                    "type": TemporalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalCS",
                    "type": VerticalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CartesianCS",
                    "type": CartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EllipsoidalCS",
                    "type": EllipsoidalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CoordinateSystemAxis",
                    "type": CoordinateSystemAxis,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompoundCRS",
                    "type": CompoundCrs,
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
                    "type": DerivedCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ProjectedCRS",
                    "type": ProjectedCrs,
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
                {
                    "name": "ConventionalUnit",
                    "type": ConventionalUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DerivedUnit",
                    "type": DerivedUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "BaseUnit",
                    "type": BaseUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "UnitDefinition",
                    "type": UnitDefinition,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DefinitionProxy",
                    "type": DefinitionProxy,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DefinitionCollection",
                    "type": DefinitionCollection,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Dictionary",
                    "type": Dictionary,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Definition",
                    "type": Definition,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Array",
                    "type": Array,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Bag",
                    "type": Bag,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )


@dataclass
class ValueArrayPropertyType:
    """
    GML property which refers to, or contains, a set of homogeneously typed Values.
    """

    choice: list[
        Union[
            Boolean,
            Category,
            Quantity,
            Count,
            BooleanList,
            CategoryList,
            QuantityList,
            CountList,
            CategoryExtent,
            QuantityExtent,
            CountExtent,
            ValueArray,
            CompositeValue,
            GenericMetaData,
            GraphStyle1,
            LabelStyle1,
            TopologyStyle1,
            GeometryStyle1,
            FeatureStyle1,
            Style,
            TopoComplex,
            TopoSolid,
            Face,
            Edge,
            Node,
            MovingObjectStatus,
            DirectedObservationAtDistance,
            DirectedObservation,
            Observation,
            RectifiedGridCoverage,
            GridCoverage,
            MultiSolidCoverage,
            MultiSurfaceCoverage,
            MultiCurveCoverage,
            MultiPointCoverage,
            FeatureCollection,
            TimeTopologyComplex,
            TimeEdge,
            TimeNode,
            TimePeriod,
            TimeInstant,
            MultiLineString,
            MultiPolygon,
            MultiSolid,
            MultiSurface,
            MultiCurve,
            MultiPoint,
            MultiGeometry,
            RectifiedGrid,
            Grid,
            GeometricComplex,
            Ring,
            LinearRing,
            Solid,
            CompositeSolid,
            OrientableSurface,
            Tin,
            TriangulatedSurface,
            PolyhedralSurface,
            Surface,
            CompositeSurface,
            Polygon,
            OrientableCurve,
            Curve,
            CompositeCurve,
            LineString,
            Point,
            TimeCalendarEra,
            TimeClock,
            TimeCalendar,
            TimeOrdinalReferenceSystem,
            TimeCoordinateSystem,
            OperationParameterGroup,
            OperationParameter,
            OperationMethod,
            Transformation,
            Conversion,
            PassThroughOperation,
            ConcatenatedOperation,
            Ellipsoid,
            PrimeMeridian,
            GeodeticDatum,
            TemporalDatum,
            VerticalDatum,
            ImageDatum,
            EngineeringDatum,
            ObliqueCartesianCs,
            CylindricalCs,
            PolarCs,
            SphericalCs,
            UserDefinedCs,
            LinearCs,
            TemporalCs,
            VerticalCs,
            CartesianCs,
            EllipsoidalCs,
            CoordinateSystemAxis,
            CompoundCrs,
            TemporalCrs,
            ImageCrs,
            EngineeringCrs,
            DerivedCrs,
            ProjectedCrs,
            GeocentricCrs,
            VerticalCrs,
            GeographicCrs,
            ConventionalUnit,
            DerivedUnit,
            BaseUnit,
            UnitDefinition,
            DefinitionProxy,
            DefinitionCollection,
            Dictionary,
            Definition,
            Array,
            Bag,
            Null,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Boolean",
                    "type": Boolean,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Category",
                    "type": Category,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Quantity",
                    "type": Quantity,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Count",
                    "type": Count,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "BooleanList",
                    "type": BooleanList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CategoryList",
                    "type": CategoryList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "QuantityList",
                    "type": QuantityList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CountList",
                    "type": CountList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CategoryExtent",
                    "type": CategoryExtent,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "QuantityExtent",
                    "type": QuantityExtent,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CountExtent",
                    "type": CountExtent,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ValueArray",
                    "type": ValueArray,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeValue",
                    "type": CompositeValue,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GenericMetaData",
                    "type": GenericMetaData,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GraphStyle",
                    "type": GraphStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LabelStyle",
                    "type": LabelStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopologyStyle",
                    "type": TopologyStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeometryStyle",
                    "type": GeometryStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureStyle",
                    "type": FeatureStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Style",
                    "type": Style,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopoComplex",
                    "type": TopoComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopoSolid",
                    "type": TopoSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Face",
                    "type": Face,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Edge",
                    "type": Edge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Node",
                    "type": Node,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MovingObjectStatus",
                    "type": MovingObjectStatus,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservationAtDistance",
                    "type": DirectedObservationAtDistance,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservation",
                    "type": DirectedObservation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Observation",
                    "type": Observation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGridCoverage",
                    "type": RectifiedGridCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GridCoverage",
                    "type": GridCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolidCoverage",
                    "type": MultiSolidCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurfaceCoverage",
                    "type": MultiSurfaceCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurveCoverage",
                    "type": MultiCurveCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPointCoverage",
                    "type": MultiPointCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureCollection",
                    "type": FeatureCollection,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeTopologyComplex",
                    "type": TimeTopologyComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeEdge",
                    "type": TimeEdge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeNode",
                    "type": TimeNode,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimePeriod",
                    "type": TimePeriod,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeInstant",
                    "type": TimeInstant,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiLineString",
                    "type": MultiLineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPolygon",
                    "type": MultiPolygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolid",
                    "type": MultiSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurface",
                    "type": MultiSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurve",
                    "type": MultiCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPoint",
                    "type": MultiPoint,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiGeometry",
                    "type": MultiGeometry,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGrid",
                    "type": RectifiedGrid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Grid",
                    "type": Grid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeometricComplex",
                    "type": GeometricComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Ring",
                    "type": Ring,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearRing",
                    "type": LinearRing,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Solid",
                    "type": Solid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSolid",
                    "type": CompositeSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableSurface",
                    "type": OrientableSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Tin",
                    "type": Tin,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TriangulatedSurface",
                    "type": TriangulatedSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolyhedralSurface",
                    "type": PolyhedralSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Surface",
                    "type": Surface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSurface",
                    "type": CompositeSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Polygon",
                    "type": Polygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableCurve",
                    "type": OrientableCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Curve",
                    "type": Curve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeCurve",
                    "type": CompositeCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Point",
                    "type": Point,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCalendarEra",
                    "type": TimeCalendarEra,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeClock",
                    "type": TimeClock,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCalendar",
                    "type": TimeCalendar,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeOrdinalReferenceSystem",
                    "type": TimeOrdinalReferenceSystem,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCoordinateSystem",
                    "type": TimeCoordinateSystem,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationParameterGroup",
                    "type": OperationParameterGroup,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationParameter",
                    "type": OperationParameter,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationMethod",
                    "type": OperationMethod,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Transformation",
                    "type": Transformation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Conversion",
                    "type": Conversion,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PassThroughOperation",
                    "type": PassThroughOperation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ConcatenatedOperation",
                    "type": ConcatenatedOperation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Ellipsoid",
                    "type": Ellipsoid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PrimeMeridian",
                    "type": PrimeMeridian,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeodeticDatum",
                    "type": GeodeticDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalDatum",
                    "type": TemporalDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalDatum",
                    "type": VerticalDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ImageDatum",
                    "type": ImageDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EngineeringDatum",
                    "type": EngineeringDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ObliqueCartesianCS",
                    "type": ObliqueCartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CylindricalCS",
                    "type": CylindricalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolarCS",
                    "type": PolarCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "SphericalCS",
                    "type": SphericalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "UserDefinedCS",
                    "type": UserDefinedCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearCS",
                    "type": LinearCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalCS",
                    "type": TemporalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalCS",
                    "type": VerticalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CartesianCS",
                    "type": CartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EllipsoidalCS",
                    "type": EllipsoidalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CoordinateSystemAxis",
                    "type": CoordinateSystemAxis,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompoundCRS",
                    "type": CompoundCrs,
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
                    "type": DerivedCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ProjectedCRS",
                    "type": ProjectedCrs,
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
                {
                    "name": "ConventionalUnit",
                    "type": ConventionalUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DerivedUnit",
                    "type": DerivedUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "BaseUnit",
                    "type": BaseUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "UnitDefinition",
                    "type": UnitDefinition,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DefinitionProxy",
                    "type": DefinitionProxy,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DefinitionCollection",
                    "type": DefinitionCollection,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Dictionary",
                    "type": Dictionary,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Definition",
                    "type": Definition,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Array",
                    "type": Array,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Bag",
                    "type": Bag,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Null",
                    "type": Null,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )


@dataclass
class ValuePropertyType:
    """
    GML property which refers to, or contains, a Value.
    """

    choice: Optional[
        Union[
            Boolean,
            Category,
            Quantity,
            Count,
            BooleanList,
            CategoryList,
            QuantityList,
            CountList,
            CategoryExtent,
            QuantityExtent,
            CountExtent,
            ValueArray,
            CompositeValue,
            GenericMetaData,
            GraphStyle1,
            LabelStyle1,
            TopologyStyle1,
            GeometryStyle1,
            FeatureStyle1,
            Style,
            TopoComplex,
            TopoSolid,
            Face,
            Edge,
            Node,
            MovingObjectStatus,
            DirectedObservationAtDistance,
            DirectedObservation,
            Observation,
            RectifiedGridCoverage,
            GridCoverage,
            MultiSolidCoverage,
            MultiSurfaceCoverage,
            MultiCurveCoverage,
            MultiPointCoverage,
            FeatureCollection,
            TimeTopologyComplex,
            TimeEdge,
            TimeNode,
            TimePeriod,
            TimeInstant,
            MultiLineString,
            MultiPolygon,
            MultiSolid,
            MultiSurface,
            MultiCurve,
            MultiPoint,
            MultiGeometry,
            RectifiedGrid,
            Grid,
            GeometricComplex,
            Ring,
            LinearRing,
            Solid,
            CompositeSolid,
            OrientableSurface,
            Tin,
            TriangulatedSurface,
            PolyhedralSurface,
            Surface,
            CompositeSurface,
            Polygon,
            OrientableCurve,
            Curve,
            CompositeCurve,
            LineString,
            Point,
            TimeCalendarEra,
            TimeClock,
            TimeCalendar,
            TimeOrdinalReferenceSystem,
            TimeCoordinateSystem,
            OperationParameterGroup,
            OperationParameter,
            OperationMethod,
            Transformation,
            Conversion,
            PassThroughOperation,
            ConcatenatedOperation,
            Ellipsoid,
            PrimeMeridian,
            GeodeticDatum,
            TemporalDatum,
            VerticalDatum,
            ImageDatum,
            EngineeringDatum,
            ObliqueCartesianCs,
            CylindricalCs,
            PolarCs,
            SphericalCs,
            UserDefinedCs,
            LinearCs,
            TemporalCs,
            VerticalCs,
            CartesianCs,
            EllipsoidalCs,
            CoordinateSystemAxis,
            CompoundCrs,
            TemporalCrs,
            ImageCrs,
            EngineeringCrs,
            DerivedCrs,
            ProjectedCrs,
            GeocentricCrs,
            VerticalCrs,
            GeographicCrs,
            ConventionalUnit,
            DerivedUnit,
            BaseUnit,
            UnitDefinition,
            DefinitionProxy,
            DefinitionCollection,
            Dictionary,
            Definition,
            Array,
            Bag,
            Null,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Boolean",
                    "type": Boolean,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Category",
                    "type": Category,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Quantity",
                    "type": Quantity,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Count",
                    "type": Count,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "BooleanList",
                    "type": BooleanList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CategoryList",
                    "type": CategoryList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "QuantityList",
                    "type": QuantityList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CountList",
                    "type": CountList,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CategoryExtent",
                    "type": CategoryExtent,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "QuantityExtent",
                    "type": QuantityExtent,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CountExtent",
                    "type": CountExtent,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ValueArray",
                    "type": ValueArray,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeValue",
                    "type": CompositeValue,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GenericMetaData",
                    "type": GenericMetaData,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GraphStyle",
                    "type": GraphStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LabelStyle",
                    "type": LabelStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopologyStyle",
                    "type": TopologyStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeometryStyle",
                    "type": GeometryStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureStyle",
                    "type": FeatureStyle1,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Style",
                    "type": Style,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopoComplex",
                    "type": TopoComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TopoSolid",
                    "type": TopoSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Face",
                    "type": Face,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Edge",
                    "type": Edge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Node",
                    "type": Node,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MovingObjectStatus",
                    "type": MovingObjectStatus,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservationAtDistance",
                    "type": DirectedObservationAtDistance,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DirectedObservation",
                    "type": DirectedObservation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Observation",
                    "type": Observation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGridCoverage",
                    "type": RectifiedGridCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GridCoverage",
                    "type": GridCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolidCoverage",
                    "type": MultiSolidCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurfaceCoverage",
                    "type": MultiSurfaceCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurveCoverage",
                    "type": MultiCurveCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPointCoverage",
                    "type": MultiPointCoverage,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "FeatureCollection",
                    "type": FeatureCollection,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeTopologyComplex",
                    "type": TimeTopologyComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeEdge",
                    "type": TimeEdge,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeNode",
                    "type": TimeNode,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimePeriod",
                    "type": TimePeriod,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeInstant",
                    "type": TimeInstant,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiLineString",
                    "type": MultiLineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPolygon",
                    "type": MultiPolygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSolid",
                    "type": MultiSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiSurface",
                    "type": MultiSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiCurve",
                    "type": MultiCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiPoint",
                    "type": MultiPoint,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "MultiGeometry",
                    "type": MultiGeometry,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "RectifiedGrid",
                    "type": RectifiedGrid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Grid",
                    "type": Grid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeometricComplex",
                    "type": GeometricComplex,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Ring",
                    "type": Ring,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearRing",
                    "type": LinearRing,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Solid",
                    "type": Solid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSolid",
                    "type": CompositeSolid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableSurface",
                    "type": OrientableSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Tin",
                    "type": Tin,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TriangulatedSurface",
                    "type": TriangulatedSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolyhedralSurface",
                    "type": PolyhedralSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Surface",
                    "type": Surface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeSurface",
                    "type": CompositeSurface,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Polygon",
                    "type": Polygon,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OrientableCurve",
                    "type": OrientableCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Curve",
                    "type": Curve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompositeCurve",
                    "type": CompositeCurve,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LineString",
                    "type": LineString,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Point",
                    "type": Point,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCalendarEra",
                    "type": TimeCalendarEra,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeClock",
                    "type": TimeClock,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCalendar",
                    "type": TimeCalendar,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeOrdinalReferenceSystem",
                    "type": TimeOrdinalReferenceSystem,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TimeCoordinateSystem",
                    "type": TimeCoordinateSystem,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationParameterGroup",
                    "type": OperationParameterGroup,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationParameter",
                    "type": OperationParameter,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationMethod",
                    "type": OperationMethod,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Transformation",
                    "type": Transformation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Conversion",
                    "type": Conversion,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PassThroughOperation",
                    "type": PassThroughOperation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ConcatenatedOperation",
                    "type": ConcatenatedOperation,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Ellipsoid",
                    "type": Ellipsoid,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PrimeMeridian",
                    "type": PrimeMeridian,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "GeodeticDatum",
                    "type": GeodeticDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalDatum",
                    "type": TemporalDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalDatum",
                    "type": VerticalDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ImageDatum",
                    "type": ImageDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EngineeringDatum",
                    "type": EngineeringDatum,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ObliqueCartesianCS",
                    "type": ObliqueCartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CylindricalCS",
                    "type": CylindricalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "PolarCS",
                    "type": PolarCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "SphericalCS",
                    "type": SphericalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "UserDefinedCS",
                    "type": UserDefinedCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "LinearCS",
                    "type": LinearCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "TemporalCS",
                    "type": TemporalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "VerticalCS",
                    "type": VerticalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CartesianCS",
                    "type": CartesianCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "EllipsoidalCS",
                    "type": EllipsoidalCs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CoordinateSystemAxis",
                    "type": CoordinateSystemAxis,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "CompoundCRS",
                    "type": CompoundCrs,
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
                    "type": DerivedCrs,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "ProjectedCRS",
                    "type": ProjectedCrs,
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
                {
                    "name": "ConventionalUnit",
                    "type": ConventionalUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DerivedUnit",
                    "type": DerivedUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "BaseUnit",
                    "type": BaseUnit,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "UnitDefinition",
                    "type": UnitDefinition,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DefinitionProxy",
                    "type": DefinitionProxy,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "DefinitionCollection",
                    "type": DefinitionCollection,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Dictionary",
                    "type": Dictionary,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Definition",
                    "type": Definition,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Array",
                    "type": Array,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Bag",
                    "type": Bag,
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "Null",
                    "type": Null,
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
class Members(ArrayAssociationType):
    class Meta:
        name = "members"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ValueComponent(ValuePropertyType):
    """Element which refers to, or contains, a Value.

    This version is used in CompositeValues.
    """

    class Meta:
        name = "valueComponent"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ValueComponents(ValueArrayPropertyType):
    """
    Element which refers to, or contains, a set of homogeneously typed Values.
    """

    class Meta:
        name = "valueComponents"
        namespace = "http://www.opengis.net/gml"
