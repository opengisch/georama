from dataclasses import dataclass, field
from typing import Any, Optional

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

    directed_observation_at_distance: list["DirectedObservationAtDistance"] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation: list["DirectedObservation"] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    observation: list["Observation"] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid_coverage: list["RectifiedGridCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_coverage: list["GridCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid_coverage: list["MultiSolidCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface_coverage: list["MultiSurfaceCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve_coverage: list["MultiCurveCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point_coverage: list["MultiPointCoverage"] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_collection: list["FeatureCollection"] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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

    directed_observation_at_distance: Optional["DirectedObservationAtDistance"] = field(
        default=None,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation: Optional["DirectedObservation"] = field(
        default=None,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    observation: Optional["Observation"] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid_coverage: Optional["RectifiedGridCoverage"] = field(
        default=None,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_coverage: Optional["GridCoverage"] = field(
        default=None,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid_coverage: Optional["MultiSolidCoverage"] = field(
        default=None,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface_coverage: Optional["MultiSurfaceCoverage"] = field(
        default=None,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve_coverage: Optional["MultiCurveCoverage"] = field(
        default=None,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point_coverage: Optional["MultiPointCoverage"] = field(
        default=None,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_collection: Optional["FeatureCollection"] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
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
    If co-occurence is not prohibited, then both a link and content may be present.  If this occurs in an instance, then the rule for interpretation is that the instance found by traversing the href provides the normative value of the property, and should be used when possible.  The value(s) included as content may be used if the remote instance cannot be resolved.  This may be considered to be a "cached" version of the value(s)."""

    generic_meta_data: Optional[GenericMetaData] = field(
        default=None,
        metadata={
            "name": "GenericMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    graph_style: Optional[GraphStyle1] = field(
        default=None,
        metadata={
            "name": "GraphStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    label_style: Optional[LabelStyle1] = field(
        default=None,
        metadata={
            "name": "LabelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topology_style: Optional[TopologyStyle1] = field(
        default=None,
        metadata={
            "name": "TopologyStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometry_style: Optional[GeometryStyle1] = field(
        default=None,
        metadata={
            "name": "GeometryStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_style: Optional[FeatureStyle1] = field(
        default=None,
        metadata={
            "name": "FeatureStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    style: Optional[Style] = field(
        default=None,
        metadata={
            "name": "Style",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_complex: Optional[TopoComplex] = field(
        default=None,
        metadata={
            "name": "TopoComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_solid: Optional[TopoSolid] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    face: Optional[Face] = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    edge: Optional[Edge] = field(
        default=None,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    node: Optional[Node] = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    moving_object_status: Optional[MovingObjectStatus] = field(
        default=None,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation_at_distance: Optional["DirectedObservationAtDistance"] = field(
        default=None,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation: Optional["DirectedObservation"] = field(
        default=None,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    observation: Optional["Observation"] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid_coverage: Optional["RectifiedGridCoverage"] = field(
        default=None,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_coverage: Optional["GridCoverage"] = field(
        default=None,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid_coverage: Optional["MultiSolidCoverage"] = field(
        default=None,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface_coverage: Optional["MultiSurfaceCoverage"] = field(
        default=None,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve_coverage: Optional["MultiCurveCoverage"] = field(
        default=None,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point_coverage: Optional["MultiPointCoverage"] = field(
        default=None,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_collection: Optional["FeatureCollection"] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_topology_complex: Optional[TimeTopologyComplex] = field(
        default=None,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_edge: Optional[TimeEdge] = field(
        default=None,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_node: Optional[TimeNode] = field(
        default=None,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_instant: Optional[TimeInstant] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_line_string: Optional[MultiLineString] = field(
        default=None,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_polygon: Optional[MultiPolygon] = field(
        default=None,
        metadata={
            "name": "MultiPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_geometry: Optional[MultiGeometry] = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid: Optional[RectifiedGrid] = field(
        default=None,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid: Optional[Grid] = field(
        default=None,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometric_complex: Optional[GeometricComplex] = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid: Optional[Solid] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: Optional[Surface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve: Optional[Curve] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point: Optional[Point] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_calendar_era: Optional[TimeCalendarEra] = field(
        default=None,
        metadata={
            "name": "TimeCalendarEra",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_clock: Optional[TimeClock] = field(
        default=None,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_calendar: Optional[TimeCalendar] = field(
        default=None,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_ordinal_reference_system: Optional[TimeOrdinalReferenceSystem] = field(
        default=None,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_coordinate_system: Optional[TimeCoordinateSystem] = field(
        default=None,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter_group: Optional[OperationParameterGroup] = field(
        default=None,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter: Optional[OperationParameter] = field(
        default=None,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_method: Optional[OperationMethod] = field(
        default=None,
        metadata={
            "name": "OperationMethod",
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
    conversion: Optional[Conversion] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pass_through_operation: Optional[PassThroughOperation] = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    concatenated_operation: Optional[ConcatenatedOperation] = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoid: Optional[Ellipsoid] = field(
        default=None,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    prime_meridian: Optional[PrimeMeridian] = field(
        default=None,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_datum: Optional[GeodeticDatum] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_datum: Optional[TemporalDatum] = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_datum: Optional[VerticalDatum] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_datum: Optional[ImageDatum] = field(
        default=None,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_datum: Optional[EngineeringDatum] = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    oblique_cartesian_cs: Optional[ObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cylindrical_cs: Optional[CylindricalCs] = field(
        default=None,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polar_cs: Optional[PolarCs] = field(
        default=None,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    spherical_cs: Optional[SphericalCs] = field(
        default=None,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    user_defined_cs: Optional[UserDefinedCs] = field(
        default=None,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_cs: Optional[LinearCs] = field(
        default=None,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_cs: Optional[TemporalCs] = field(
        default=None,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_cs: Optional[VerticalCs] = field(
        default=None,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cartesian_cs: Optional[CartesianCs] = field(
        default=None,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoidal_cs: Optional[EllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinate_system_axis: Optional[CoordinateSystemAxis] = field(
        default=None,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    compound_crs: Optional[CompoundCrs] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conventional_unit: Optional[ConventionalUnit] = field(
        default=None,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_unit: Optional[DerivedUnit] = field(
        default=None,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    base_unit: Optional[BaseUnit] = field(
        default=None,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    unit_definition: Optional[UnitDefinition] = field(
        default=None,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_proxy: Optional[DefinitionProxy] = field(
        default=None,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_collection: Optional[DefinitionCollection] = field(
        default=None,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dictionary: Optional[Dictionary] = field(
        default=None,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition: Optional[Definition] = field(
        default=None,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    array: Optional[Array] = field(
        default=None,
        metadata={
            "name": "Array",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bag: Optional[Bag] = field(
        default=None,
        metadata={
            "name": "Bag",
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

    boolean: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category: Optional[Category] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count: Optional[Count] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_list: Optional[BooleanList] = field(
        default=None,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_list: Optional[CategoryList] = field(
        default=None,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_list: Optional[QuantityList] = field(
        default=None,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_list: Optional[CountList] = field(
        default=None,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_extent: Optional[CategoryExtent] = field(
        default=None,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_extent: Optional[QuantityExtent] = field(
        default=None,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_extent: Optional[CountExtent] = field(
        default=None,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_array: Optional[ValueArray] = field(
        default=None,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_value: Optional[CompositeValue] = field(
        default=None,
        metadata={
            "name": "CompositeValue",
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
    tuple_list: Optional[TupleList] = field(
        default=None,
        metadata={
            "name": "tupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    double_or_null_tuple_list: Optional[DoubleOrNullTupleList] = field(
        default=None,
        metadata={
            "name": "doubleOrNullTupleList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    """
    :ivar value_array: each member _Value holds a tuple or "row" from
        the equivalent table
    :ivar boolean_list:
    :ivar category_list:
    :ivar quantity_list:
    :ivar count_list:
    :ivar data_block: Its tuple list holds the values as space-separated
        tuples each of which contains comma-separated components, and
        the tuple structure is specified using the rangeParameters
        property.
    :ivar file: a reference to an external source for the data, together
        with a description of how that external source is structured
    """

    value_array: list[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_list: list[BooleanList] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_list: list[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_list: list[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_list: list[CountList] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    data_block: Optional[DataBlock] = field(
        default=None,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    file: Optional[File] = field(
        default=None,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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

    rectified_grid_domain: Optional[RectifiedGridDomain] = field(
        default=None,
        metadata={
            "name": "rectifiedGridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_domain: Optional[GridDomain] = field(
        default=None,
        metadata={
            "name": "gridDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid_domain: Optional[MultiSolidDomain] = field(
        default=None,
        metadata={
            "name": "multiSolidDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface_domain: Optional[MultiSurfaceDomain] = field(
        default=None,
        metadata={
            "name": "multiSurfaceDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve_domain: Optional[MultiCurveDomain] = field(
        default=None,
        metadata={
            "name": "multiCurveDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point_domain: Optional[MultiPointDomain] = field(
        default=None,
        metadata={
            "name": "multiPointDomain",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    domain_set: Optional[DomainSet] = field(
        default=None,
        metadata={
            "name": "domainSet",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    """
    :ivar rectified_grid_domain:
    :ivar multi_solid_domain:
    :ivar multi_surface_domain:
    :ivar multi_curve_domain:
    :ivar multi_point_domain:
    :ivar domain_set:
    :ivar priority_location:
    :ivar location: deprecated in GML version 3.1
    :ivar grid_domain:
    """

    rectified_grid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_surface_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_point_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    domain_set: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    location: Any = field(
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

    :ivar rectified_grid_domain:
    :ivar grid_domain:
    :ivar multi_solid_domain:
    :ivar multi_surface_domain:
    :ivar multi_point_domain:
    :ivar domain_set:
    :ivar priority_location:
    :ivar location: deprecated in GML version 3.1
    :ivar multi_curve_domain:
    """

    rectified_grid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    grid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_surface_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_point_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    domain_set: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    location: Any = field(
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

    :ivar rectified_grid_domain:
    :ivar grid_domain:
    :ivar multi_solid_domain:
    :ivar multi_surface_domain:
    :ivar multi_curve_domain:
    :ivar domain_set:
    :ivar priority_location:
    :ivar location: deprecated in GML version 3.1
    :ivar multi_point_domain:
    """

    rectified_grid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    grid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_surface_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    domain_set: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    location: Any = field(
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

    :ivar rectified_grid_domain:
    :ivar grid_domain:
    :ivar multi_surface_domain:
    :ivar multi_curve_domain:
    :ivar multi_point_domain:
    :ivar domain_set:
    :ivar priority_location:
    :ivar location: deprecated in GML version 3.1
    :ivar multi_solid_domain:
    """

    rectified_grid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    grid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_surface_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_point_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    domain_set: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    location: Any = field(
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

    :ivar rectified_grid_domain:
    :ivar grid_domain:
    :ivar multi_solid_domain:
    :ivar multi_curve_domain:
    :ivar multi_point_domain:
    :ivar domain_set:
    :ivar priority_location:
    :ivar location: deprecated in GML version 3.1
    :ivar multi_surface_domain:
    """

    rectified_grid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    grid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_point_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    domain_set: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    location: Any = field(
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
    """
    :ivar grid_domain:
    :ivar multi_solid_domain:
    :ivar multi_surface_domain:
    :ivar multi_curve_domain:
    :ivar multi_point_domain:
    :ivar domain_set:
    :ivar priority_location:
    :ivar location: deprecated in GML version 3.1
    :ivar rectified_grid_domain:
    """

    grid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_surface_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_point_domain: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    domain_set: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    priority_location: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    location: Any = field(
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

    directed_observation_at_distance: Optional["DirectedObservationAtDistance"] = field(
        default=None,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation: Optional["DirectedObservation"] = field(
        default=None,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    observation: Optional["Observation"] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid_coverage: Optional[RectifiedGridCoverage] = field(
        default=None,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_coverage: Optional[GridCoverage] = field(
        default=None,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid_coverage: Optional[MultiSolidCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface_coverage: Optional[MultiSurfaceCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve_coverage: Optional[MultiCurveCoverage] = field(
        default=None,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point_coverage: Optional[MultiPointCoverage] = field(
        default=None,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_line_string: Optional[MultiLineString] = field(
        default=None,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_polygon: Optional[MultiPolygon] = field(
        default=None,
        metadata={
            "name": "MultiPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_geometry: Optional[MultiGeometry] = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid: Optional[RectifiedGrid] = field(
        default=None,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid: Optional[Grid] = field(
        default=None,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometric_complex: Optional[GeometricComplex] = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid: Optional[Solid] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: Optional[Surface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve: Optional[Curve] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point: Optional[Point] = field(
        default=None,
        metadata={
            "name": "Point",
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
    subject: Optional[Subject] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    target: Optional[Target] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
    However, this leads to a non-deterministic content model, since both the base and the extension have minOccurs="0", and is thus prohibited in XML Schema."""

    generic_meta_data: list[GenericMetaData] = field(
        default_factory=list,
        metadata={
            "name": "GenericMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    graph_style: list[GraphStyle1] = field(
        default_factory=list,
        metadata={
            "name": "GraphStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    label_style: list[LabelStyle1] = field(
        default_factory=list,
        metadata={
            "name": "LabelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topology_style: list[TopologyStyle1] = field(
        default_factory=list,
        metadata={
            "name": "TopologyStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometry_style: list[GeometryStyle1] = field(
        default_factory=list,
        metadata={
            "name": "GeometryStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_style: list[FeatureStyle1] = field(
        default_factory=list,
        metadata={
            "name": "FeatureStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    style: list[Style] = field(
        default_factory=list,
        metadata={
            "name": "Style",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_complex: list[TopoComplex] = field(
        default_factory=list,
        metadata={
            "name": "TopoComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_solid: list[TopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    face: list[Face] = field(
        default_factory=list,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    edge: list[Edge] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    node: list[Node] = field(
        default_factory=list,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    moving_object_status: list[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation_at_distance: list[DirectedObservationAtDistance] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation: list[DirectedObservation] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    observation: list[Observation] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid_coverage: list[RectifiedGridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_coverage: list[GridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid_coverage: list[MultiSolidCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface_coverage: list[MultiSurfaceCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve_coverage: list[MultiCurveCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point_coverage: list[MultiPointCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_collection: list[FeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_topology_complex: list[TimeTopologyComplex] = field(
        default_factory=list,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_edge: list[TimeEdge] = field(
        default_factory=list,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_node: list[TimeNode] = field(
        default_factory=list,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_period: list[TimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_instant: list[TimeInstant] = field(
        default_factory=list,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_line_string: list[MultiLineString] = field(
        default_factory=list,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_polygon: list[MultiPolygon] = field(
        default_factory=list,
        metadata={
            "name": "MultiPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid: list[MultiSolid] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface: list[MultiSurface] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve: list[MultiCurve] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point: list[MultiPoint] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_geometry: list[MultiGeometry] = field(
        default_factory=list,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid: list[RectifiedGrid] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid: list[Grid] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometric_complex: list[GeometricComplex] = field(
        default_factory=list,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ring: list[Ring] = field(
        default_factory=list,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_ring: list[LinearRing] = field(
        default_factory=list,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid: list[Solid] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_solid: list[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_surface: list[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: list[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: list[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: list[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: list[Surface] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: list[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_curve: list[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve: list[Curve] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_curve: list[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string: list[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_calendar_era: list[TimeCalendarEra] = field(
        default_factory=list,
        metadata={
            "name": "TimeCalendarEra",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_clock: list[TimeClock] = field(
        default_factory=list,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_calendar: list[TimeCalendar] = field(
        default_factory=list,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_ordinal_reference_system: list[TimeOrdinalReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_coordinate_system: list[TimeCoordinateSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter_group: list[OperationParameterGroup] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter: list[OperationParameter] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_method: list[OperationMethod] = field(
        default_factory=list,
        metadata={
            "name": "OperationMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    transformation: list[Transformation] = field(
        default_factory=list,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conversion: list[Conversion] = field(
        default_factory=list,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pass_through_operation: list[PassThroughOperation] = field(
        default_factory=list,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    concatenated_operation: list[ConcatenatedOperation] = field(
        default_factory=list,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoid: list[Ellipsoid] = field(
        default_factory=list,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    prime_meridian: list[PrimeMeridian] = field(
        default_factory=list,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_datum: list[GeodeticDatum] = field(
        default_factory=list,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_datum: list[TemporalDatum] = field(
        default_factory=list,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_datum: list[VerticalDatum] = field(
        default_factory=list,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_datum: list[ImageDatum] = field(
        default_factory=list,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_datum: list[EngineeringDatum] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    oblique_cartesian_cs: list[ObliqueCartesianCs] = field(
        default_factory=list,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cylindrical_cs: list[CylindricalCs] = field(
        default_factory=list,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polar_cs: list[PolarCs] = field(
        default_factory=list,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    spherical_cs: list[SphericalCs] = field(
        default_factory=list,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    user_defined_cs: list[UserDefinedCs] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_cs: list[LinearCs] = field(
        default_factory=list,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_cs: list[TemporalCs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_cs: list[VerticalCs] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cartesian_cs: list[CartesianCs] = field(
        default_factory=list,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoidal_cs: list[EllipsoidalCs] = field(
        default_factory=list,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinate_system_axis: list[CoordinateSystemAxis] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    compound_crs: list[CompoundCrs] = field(
        default_factory=list,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_crs: list[TemporalCrs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_crs: list[ImageCrs] = field(
        default_factory=list,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_crs: list[EngineeringCrs] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_crs: list[DerivedCrs] = field(
        default_factory=list,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    projected_crs: list[ProjectedCrs] = field(
        default_factory=list,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geocentric_crs: list[GeocentricCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_crs: list[VerticalCrs] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geographic_crs: list[GeographicCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conventional_unit: list[ConventionalUnit] = field(
        default_factory=list,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_unit: list[DerivedUnit] = field(
        default_factory=list,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    base_unit: list[BaseUnit] = field(
        default_factory=list,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    unit_definition: list[UnitDefinition] = field(
        default_factory=list,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_proxy: list[DefinitionProxy] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_collection: list[DefinitionCollection] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dictionary: list[Dictionary] = field(
        default_factory=list,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition: list[Definition] = field(
        default_factory=list,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "name": "Array",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bag: list[Bag] = field(
        default_factory=list,
        metadata={
            "name": "Bag",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class ValueArrayPropertyType:
    """
    GML property which refers to, or contains, a set of homogeneously typed Values.
    """

    boolean: list[Boolean] = field(
        default_factory=list,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category: list[Category] = field(
        default_factory=list,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity: list[Quantity] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count: list[Count] = field(
        default_factory=list,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_list: list[BooleanList] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_list: list[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_list: list[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_list: list[CountList] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_extent: list[CategoryExtent] = field(
        default_factory=list,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_extent: list[QuantityExtent] = field(
        default_factory=list,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_extent: list[CountExtent] = field(
        default_factory=list,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_array: list[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_value: list[CompositeValue] = field(
        default_factory=list,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    generic_meta_data: list[GenericMetaData] = field(
        default_factory=list,
        metadata={
            "name": "GenericMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    graph_style: list[GraphStyle1] = field(
        default_factory=list,
        metadata={
            "name": "GraphStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    label_style: list[LabelStyle1] = field(
        default_factory=list,
        metadata={
            "name": "LabelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topology_style: list[TopologyStyle1] = field(
        default_factory=list,
        metadata={
            "name": "TopologyStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometry_style: list[GeometryStyle1] = field(
        default_factory=list,
        metadata={
            "name": "GeometryStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_style: list[FeatureStyle1] = field(
        default_factory=list,
        metadata={
            "name": "FeatureStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    style: list[Style] = field(
        default_factory=list,
        metadata={
            "name": "Style",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_complex: list[TopoComplex] = field(
        default_factory=list,
        metadata={
            "name": "TopoComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_solid: list[TopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    face: list[Face] = field(
        default_factory=list,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    edge: list[Edge] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    node: list[Node] = field(
        default_factory=list,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    moving_object_status: list[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation_at_distance: list[DirectedObservationAtDistance] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation: list[DirectedObservation] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    observation: list[Observation] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid_coverage: list[RectifiedGridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_coverage: list[GridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid_coverage: list[MultiSolidCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface_coverage: list[MultiSurfaceCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve_coverage: list[MultiCurveCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point_coverage: list[MultiPointCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_collection: list[FeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_topology_complex: list[TimeTopologyComplex] = field(
        default_factory=list,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_edge: list[TimeEdge] = field(
        default_factory=list,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_node: list[TimeNode] = field(
        default_factory=list,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_period: list[TimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_instant: list[TimeInstant] = field(
        default_factory=list,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_line_string: list[MultiLineString] = field(
        default_factory=list,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_polygon: list[MultiPolygon] = field(
        default_factory=list,
        metadata={
            "name": "MultiPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid: list[MultiSolid] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface: list[MultiSurface] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve: list[MultiCurve] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point: list[MultiPoint] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_geometry: list[MultiGeometry] = field(
        default_factory=list,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid: list[RectifiedGrid] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid: list[Grid] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometric_complex: list[GeometricComplex] = field(
        default_factory=list,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ring: list[Ring] = field(
        default_factory=list,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_ring: list[LinearRing] = field(
        default_factory=list,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid: list[Solid] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_solid: list[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_surface: list[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: list[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: list[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: list[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: list[Surface] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: list[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_curve: list[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve: list[Curve] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_curve: list[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string: list[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_calendar_era: list[TimeCalendarEra] = field(
        default_factory=list,
        metadata={
            "name": "TimeCalendarEra",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_clock: list[TimeClock] = field(
        default_factory=list,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_calendar: list[TimeCalendar] = field(
        default_factory=list,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_ordinal_reference_system: list[TimeOrdinalReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_coordinate_system: list[TimeCoordinateSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter_group: list[OperationParameterGroup] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter: list[OperationParameter] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_method: list[OperationMethod] = field(
        default_factory=list,
        metadata={
            "name": "OperationMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    transformation: list[Transformation] = field(
        default_factory=list,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conversion: list[Conversion] = field(
        default_factory=list,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pass_through_operation: list[PassThroughOperation] = field(
        default_factory=list,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    concatenated_operation: list[ConcatenatedOperation] = field(
        default_factory=list,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoid: list[Ellipsoid] = field(
        default_factory=list,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    prime_meridian: list[PrimeMeridian] = field(
        default_factory=list,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_datum: list[GeodeticDatum] = field(
        default_factory=list,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_datum: list[TemporalDatum] = field(
        default_factory=list,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_datum: list[VerticalDatum] = field(
        default_factory=list,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_datum: list[ImageDatum] = field(
        default_factory=list,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_datum: list[EngineeringDatum] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    oblique_cartesian_cs: list[ObliqueCartesianCs] = field(
        default_factory=list,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cylindrical_cs: list[CylindricalCs] = field(
        default_factory=list,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polar_cs: list[PolarCs] = field(
        default_factory=list,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    spherical_cs: list[SphericalCs] = field(
        default_factory=list,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    user_defined_cs: list[UserDefinedCs] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_cs: list[LinearCs] = field(
        default_factory=list,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_cs: list[TemporalCs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_cs: list[VerticalCs] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cartesian_cs: list[CartesianCs] = field(
        default_factory=list,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoidal_cs: list[EllipsoidalCs] = field(
        default_factory=list,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinate_system_axis: list[CoordinateSystemAxis] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    compound_crs: list[CompoundCrs] = field(
        default_factory=list,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_crs: list[TemporalCrs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_crs: list[ImageCrs] = field(
        default_factory=list,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_crs: list[EngineeringCrs] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_crs: list[DerivedCrs] = field(
        default_factory=list,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    projected_crs: list[ProjectedCrs] = field(
        default_factory=list,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geocentric_crs: list[GeocentricCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_crs: list[VerticalCrs] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geographic_crs: list[GeographicCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conventional_unit: list[ConventionalUnit] = field(
        default_factory=list,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_unit: list[DerivedUnit] = field(
        default_factory=list,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    base_unit: list[BaseUnit] = field(
        default_factory=list,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    unit_definition: list[UnitDefinition] = field(
        default_factory=list,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_proxy: list[DefinitionProxy] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_collection: list[DefinitionCollection] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dictionary: list[Dictionary] = field(
        default_factory=list,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition: list[Definition] = field(
        default_factory=list,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    array: list[Array] = field(
        default_factory=list,
        metadata={
            "name": "Array",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bag: list[Bag] = field(
        default_factory=list,
        metadata={
            "name": "Bag",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    null: list[Null] = field(
        default_factory=list,
        metadata={
            "name": "Null",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class ValuePropertyType:
    """
    GML property which refers to, or contains, a Value.
    """

    boolean: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category: Optional[Category] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count: Optional[Count] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_list: Optional[BooleanList] = field(
        default=None,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_list: Optional[CategoryList] = field(
        default=None,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_list: Optional[QuantityList] = field(
        default=None,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_list: Optional[CountList] = field(
        default=None,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_extent: Optional[CategoryExtent] = field(
        default=None,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_extent: Optional[QuantityExtent] = field(
        default=None,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_extent: Optional[CountExtent] = field(
        default=None,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_array: Optional[ValueArray] = field(
        default=None,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_value: Optional[CompositeValue] = field(
        default=None,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    generic_meta_data: Optional[GenericMetaData] = field(
        default=None,
        metadata={
            "name": "GenericMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    graph_style: Optional[GraphStyle1] = field(
        default=None,
        metadata={
            "name": "GraphStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    label_style: Optional[LabelStyle1] = field(
        default=None,
        metadata={
            "name": "LabelStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topology_style: Optional[TopologyStyle1] = field(
        default=None,
        metadata={
            "name": "TopologyStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometry_style: Optional[GeometryStyle1] = field(
        default=None,
        metadata={
            "name": "GeometryStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_style: Optional[FeatureStyle1] = field(
        default=None,
        metadata={
            "name": "FeatureStyle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    style: Optional[Style] = field(
        default=None,
        metadata={
            "name": "Style",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_complex: Optional[TopoComplex] = field(
        default=None,
        metadata={
            "name": "TopoComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_solid: Optional[TopoSolid] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    face: Optional[Face] = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    edge: Optional[Edge] = field(
        default=None,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    node: Optional[Node] = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    moving_object_status: Optional[MovingObjectStatus] = field(
        default=None,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation_at_distance: Optional[DirectedObservationAtDistance] = field(
        default=None,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation: Optional[DirectedObservation] = field(
        default=None,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    observation: Optional[Observation] = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid_coverage: Optional[RectifiedGridCoverage] = field(
        default=None,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_coverage: Optional[GridCoverage] = field(
        default=None,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid_coverage: Optional[MultiSolidCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface_coverage: Optional[MultiSurfaceCoverage] = field(
        default=None,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve_coverage: Optional[MultiCurveCoverage] = field(
        default=None,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point_coverage: Optional[MultiPointCoverage] = field(
        default=None,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_collection: Optional[FeatureCollection] = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_topology_complex: Optional[TimeTopologyComplex] = field(
        default=None,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_edge: Optional[TimeEdge] = field(
        default=None,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_node: Optional[TimeNode] = field(
        default=None,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_period: Optional[TimePeriod] = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_instant: Optional[TimeInstant] = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_line_string: Optional[MultiLineString] = field(
        default=None,
        metadata={
            "name": "MultiLineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_polygon: Optional[MultiPolygon] = field(
        default=None,
        metadata={
            "name": "MultiPolygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid: Optional[MultiSolid] = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface: Optional[MultiSurface] = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve: Optional[MultiCurve] = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point: Optional[MultiPoint] = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_geometry: Optional[MultiGeometry] = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid: Optional[RectifiedGrid] = field(
        default=None,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid: Optional[Grid] = field(
        default=None,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometric_complex: Optional[GeometricComplex] = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ring: Optional[Ring] = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_ring: Optional[LinearRing] = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid: Optional[Solid] = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_surface: Optional[OrientableSurface] = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: Optional[Tin] = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: Optional[TriangulatedSurface] = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: Optional[PolyhedralSurface] = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: Optional[Surface] = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_curve: Optional[OrientableCurve] = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve: Optional[Curve] = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_curve: Optional[CompositeCurve] = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string: Optional[LineString] = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point: Optional[Point] = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_calendar_era: Optional[TimeCalendarEra] = field(
        default=None,
        metadata={
            "name": "TimeCalendarEra",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_clock: Optional[TimeClock] = field(
        default=None,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_calendar: Optional[TimeCalendar] = field(
        default=None,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_ordinal_reference_system: Optional[TimeOrdinalReferenceSystem] = field(
        default=None,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_coordinate_system: Optional[TimeCoordinateSystem] = field(
        default=None,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter_group: Optional[OperationParameterGroup] = field(
        default=None,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter: Optional[OperationParameter] = field(
        default=None,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_method: Optional[OperationMethod] = field(
        default=None,
        metadata={
            "name": "OperationMethod",
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
    conversion: Optional[Conversion] = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pass_through_operation: Optional[PassThroughOperation] = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    concatenated_operation: Optional[ConcatenatedOperation] = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoid: Optional[Ellipsoid] = field(
        default=None,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    prime_meridian: Optional[PrimeMeridian] = field(
        default=None,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_datum: Optional[GeodeticDatum] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_datum: Optional[TemporalDatum] = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_datum: Optional[VerticalDatum] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_datum: Optional[ImageDatum] = field(
        default=None,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_datum: Optional[EngineeringDatum] = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    oblique_cartesian_cs: Optional[ObliqueCartesianCs] = field(
        default=None,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cylindrical_cs: Optional[CylindricalCs] = field(
        default=None,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polar_cs: Optional[PolarCs] = field(
        default=None,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    spherical_cs: Optional[SphericalCs] = field(
        default=None,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    user_defined_cs: Optional[UserDefinedCs] = field(
        default=None,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_cs: Optional[LinearCs] = field(
        default=None,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_cs: Optional[TemporalCs] = field(
        default=None,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_cs: Optional[VerticalCs] = field(
        default=None,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cartesian_cs: Optional[CartesianCs] = field(
        default=None,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoidal_cs: Optional[EllipsoidalCs] = field(
        default=None,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinate_system_axis: Optional[CoordinateSystemAxis] = field(
        default=None,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    compound_crs: Optional[CompoundCrs] = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_crs: Optional[TemporalCrs] = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_crs: Optional[ImageCrs] = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_crs: Optional[EngineeringCrs] = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_crs: Optional[DerivedCrs] = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    projected_crs: Optional[ProjectedCrs] = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geographic_crs: Optional[GeographicCrs] = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conventional_unit: Optional[ConventionalUnit] = field(
        default=None,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_unit: Optional[DerivedUnit] = field(
        default=None,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    base_unit: Optional[BaseUnit] = field(
        default=None,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    unit_definition: Optional[UnitDefinition] = field(
        default=None,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_proxy: Optional[DefinitionProxy] = field(
        default=None,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_collection: Optional[DefinitionCollection] = field(
        default=None,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dictionary: Optional[Dictionary] = field(
        default=None,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition: Optional[Definition] = field(
        default=None,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    array: Optional[Array] = field(
        default=None,
        metadata={
            "name": "Array",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bag: Optional[Bag] = field(
        default=None,
        metadata={
            "name": "Bag",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    null: Optional[Null] = field(
        default=None,
        metadata={
            "name": "Null",
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
