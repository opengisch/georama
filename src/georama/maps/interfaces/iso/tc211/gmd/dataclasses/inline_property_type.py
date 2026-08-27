from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_operation_parameter_property_type import (
    OperationParameterGroup,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_parameter_value_property_type import (
    ParameterValueGroup,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_time_primitive_type import (
    TimeEdge,
    TimeInstant,
    TimeNode,
    TimePeriod,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_topo_primitive_type import (
    Edge,
    Face,
    Node,
    TopoSolid,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.affine_cs_1 import AffineCs1
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.affine_placement import (
    AffinePlacement,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.arc import Arc
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.arc_by_bulge import ArcByBulge
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.arc_by_center_point import (
    ArcByCenterPoint,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.arc_string import ArcString
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.arc_string_by_bulge import (
    ArcStringByBulge,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.array_association_type import (
    Array,
    Bag,
    DirectedObservation,
    DirectedObservationAtDistance,
    FeatureCollection,
    Observation,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.base_unit import BaseUnit
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.bezier import Bezier
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.boolean_1 import Boolean1
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.boolean_list import BooleanList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.bspline import Bspline
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cartesian_cs_1 import (
    CartesianCs1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.category import Category
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.category_extent import (
    CategoryExtent,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.category_list import CategoryList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.circle import Circle
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.circle_by_center_point import (
    CircleByCenterPoint,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.clothoid import Clothoid
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.conventional_unit import (
    ConventionalUnit,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinate_operation_property_type import (
    ConcatenatedOperation,
    PassThroughOperation,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coordinate_system_axis import (
    CoordinateSystemAxis,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.count import Count
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.count_extent import CountExtent
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.count_list import CountList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coverage_function import (
    CoverageFunction,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.coverage_mapping_rule import (
    CoverageMappingRule,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cubic_spline import CubicSpline
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.curve_property_type import (
    CompositeCurve,
    Curve,
    OffsetCurve,
    OrientableCurve,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cylindrical_cs import (
    CylindricalCs,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.data_block import DataBlock
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition import Definition
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_proxy import (
    DefinitionProxy,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.derived_unit import DerivedUnit
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dictionary_type import (
    DefinitionCollection,
    Dictionary,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dynamic_feature import (
    DynamicFeature,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dynamic_feature_collection_type import (
    DynamicFeatureCollection,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ellipsoid_1 import Ellipsoid1
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ellipsoidal_cs_1 import (
    EllipsoidalCs1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.envelope import Envelope
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.envelope_with_time_period import (
    EnvelopeWithTimePeriod,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.file import File
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.generic_meta_data import (
    GenericMetaData,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.geodesic import Geodesic
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.geodesic_string import (
    GeodesicString,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.geometric_complex import (
    GeometricComplex,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.geometry_array_property_type import (
    MultiGeometry,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.grid import Grid
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.grid_coverage import GridCoverage
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.grid_function import GridFunction
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.line_string import LineString
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.line_string_segment import (
    LineStringSegment,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.linear_cs import LinearCs
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.linear_ring import LinearRing
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.moving_object_status import (
    MovingObjectStatus,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_curve import MultiCurve
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_curve_coverage import (
    MultiCurveCoverage,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_point import MultiPoint
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_point_coverage import (
    MultiPointCoverage,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_solid import MultiSolid
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_solid_coverage import (
    MultiSolidCoverage,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_surface import MultiSurface
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.multi_surface_coverage import (
    MultiSurfaceCoverage,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.oblique_cartesian_cs import (
    ObliqueCartesianCs,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_method import (
    OperationMethod,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_parameter_1 import (
    OperationParameter1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.parameter_value_1 import (
    ParameterValue1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.point import Point
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polar_cs import PolarCs
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polygon import Polygon
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polyhedral_surface import (
    PolyhedralSurface,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.prime_meridian_1 import (
    PrimeMeridian1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.quantity import Quantity
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.quantity_extent import (
    QuantityExtent,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.quantity_list import QuantityList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.rectified_grid import (
    RectifiedGrid,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.rectified_grid_coverage import (
    RectifiedGridCoverage,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ring import Ring
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.sc_crs_property_type import (
    CompoundCrs,
    Conversion1,
    DerivedCrs,
    EngineeringCrs,
    EngineeringDatum1,
    GeocentricCrs,
    GeodeticCrs,
    GeodeticDatum1,
    GeographicCrs,
    ImageCrs,
    ImageDatum1,
    ProjectedCrs,
    TemporalCrs,
    TemporalDatum1,
    VerticalCrs,
    VerticalDatum1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.shell import Shell
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.solid import Solid
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.solid_property_type import (
    CompositeSolid,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.spherical_cs_1 import (
    SphericalCs1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface import Surface
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.surface_property_type import (
    CompositeSurface,
    OrientableSurface,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.temporal_cs import TemporalCs
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_calendar import TimeCalendar
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_clock import TimeClock
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_coordinate_system import (
    TimeCoordinateSystem,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_cs_1 import TimeCs1
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_ordinal_reference_system import (
    TimeOrdinalReferenceSystem,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_reference_system import (
    TimeReferenceSystem,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.time_topology_complex import (
    TimeTopologyComplex,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.tin import Tin
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.topo_complex_type import (
    TopoComplex,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.transformation import (
    Transformation,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.triangulated_surface import (
    TriangulatedSurface,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.unit_definition import (
    UnitDefinition,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.user_defined_cs import (
    UserDefinedCs,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.value_array_property_type import (
    CompositeValue,
    ValueArray,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vertical_cs_1 import VerticalCs1

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class InlinePropertyType:
    parameter_value_group: ParameterValueGroup | None = field(
        default=None,
        metadata={
            "name": "ParameterValueGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    parameter_value: ParameterValue1 | None = field(
        default=None,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_function: GridFunction | None = field(
        default=None,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coverage_mapping_rule: CoverageMappingRule | None = field(
        default=None,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coverage_function: CoverageFunction | None = field(
        default=None,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    file: File | None = field(
        default=None,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    data_block: DataBlock | None = field(
        default=None,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_extent: QuantityExtent | None = field(
        default=None,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_extent: CountExtent | None = field(
        default=None,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_extent: CategoryExtent | None = field(
        default=None,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_array: ValueArray | None = field(
        default=None,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_value: CompositeValue | None = field(
        default=None,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_list: QuantityList | None = field(
        default=None,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_list: CountList | None = field(
        default=None,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_list: CategoryList | None = field(
        default=None,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_list: BooleanList | None = field(
        default=None,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity: Quantity | None = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    count: Count | None = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    category: Category | None = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    boolean: Boolean1 | None = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    shell: Shell | None = field(
        default=None,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    affine_placement: AffinePlacement | None = field(
        default=None,
        metadata={
            "name": "AffinePlacement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodesic: Geodesic | None = field(
        default=None,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodesic_string: GeodesicString | None = field(
        default=None,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    clothoid: Clothoid | None = field(
        default=None,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    offset_curve: OffsetCurve | None = field(
        default=None,
        metadata={
            "name": "OffsetCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bezier: Bezier | None = field(
        default=None,
        metadata={
            "name": "Bezier",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bspline: Bspline | None = field(
        default=None,
        metadata={
            "name": "BSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cubic_spline: CubicSpline | None = field(
        default=None,
        metadata={
            "name": "CubicSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    circle_by_center_point: CircleByCenterPoint | None = field(
        default=None,
        metadata={
            "name": "CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_by_center_point: ArcByCenterPoint | None = field(
        default=None,
        metadata={
            "name": "ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_by_bulge: ArcByBulge | None = field(
        default=None,
        metadata={
            "name": "ArcByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_string_by_bulge: ArcStringByBulge | None = field(
        default=None,
        metadata={
            "name": "ArcStringByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    circle: Circle | None = field(
        default=None,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc: Arc | None = field(
        default=None,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_string: ArcString | None = field(
        default=None,
        metadata={
            "name": "ArcString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string_segment: LineStringSegment | None = field(
        default=None,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ring: Ring | None = field(
        default=None,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_ring: LinearRing | None = field(
        default=None,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope_with_time_period: EnvelopeWithTimePeriod | None = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope: Envelope | None = field(
        default=None,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    generic_meta_data: GenericMetaData | None = field(
        default=None,
        metadata={
            "name": "GenericMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_complex: TopoComplex | None = field(
        default=None,
        metadata={
            "name": "TopoComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_solid: TopoSolid | None = field(
        default=None,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    face: Face | None = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    edge: Edge | None = field(
        default=None,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    node: Node | None = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    moving_object_status: MovingObjectStatus | None = field(
        default=None,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation_at_distance: DirectedObservationAtDistance | None = field(
        default=None,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation: DirectedObservation | None = field(
        default=None,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    observation: Observation | None = field(
        default=None,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid_coverage: RectifiedGridCoverage | None = field(
        default=None,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_coverage: GridCoverage | None = field(
        default=None,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid_coverage: MultiSolidCoverage | None = field(
        default=None,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface_coverage: MultiSurfaceCoverage | None = field(
        default=None,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve_coverage: MultiCurveCoverage | None = field(
        default=None,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point_coverage: MultiPointCoverage | None = field(
        default=None,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dynamic_feature_collection: DynamicFeatureCollection | None = field(
        default=None,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dynamic_feature: DynamicFeature | None = field(
        default=None,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_collection: FeatureCollection | None = field(
        default=None,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_topology_complex: TimeTopologyComplex | None = field(
        default=None,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_edge: TimeEdge | None = field(
        default=None,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_node: TimeNode | None = field(
        default=None,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_period: TimePeriod | None = field(
        default=None,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_instant: TimeInstant | None = field(
        default=None,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid: RectifiedGrid | None = field(
        default=None,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid: Grid | None = field(
        default=None,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometric_complex: GeometricComplex | None = field(
        default=None,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid: MultiSolid | None = field(
        default=None,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface: MultiSurface | None = field(
        default=None,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve: MultiCurve | None = field(
        default=None,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point: MultiPoint | None = field(
        default=None,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_geometry: MultiGeometry | None = field(
        default=None,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_solid: CompositeSolid | None = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid: Solid | None = field(
        default=None,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: CompositeSurface | None = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_surface: OrientableSurface | None = field(
        default=None,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: Tin | None = field(
        default=None,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: TriangulatedSurface | None = field(
        default=None,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: PolyhedralSurface | None = field(
        default=None,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: Surface | None = field(
        default=None,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: Polygon | None = field(
        default=None,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_curve: CompositeCurve | None = field(
        default=None,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_curve: OrientableCurve | None = field(
        default=None,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve: Curve | None = field(
        default=None,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string: LineString | None = field(
        default=None,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point: Point | None = field(
        default=None,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_ordinal_reference_system: TimeOrdinalReferenceSystem | None = field(
        default=None,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_clock: TimeClock | None = field(
        default=None,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_calendar: TimeCalendar | None = field(
        default=None,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_coordinate_system: TimeCoordinateSystem | None = field(
        default=None,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_reference_system: TimeReferenceSystem | None = field(
        default=None,
        metadata={
            "name": "TimeReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter_group: OperationParameterGroup | None = field(
        default=None,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter: OperationParameter1 | None = field(
        default=None,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_method: OperationMethod | None = field(
        default=None,
        metadata={
            "name": "OperationMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    concatenated_operation: ConcatenatedOperation | None = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pass_through_operation: PassThroughOperation | None = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    transformation: Transformation | None = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conversion: Conversion1 | None = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    prime_meridian: PrimeMeridian1 | None = field(
        default=None,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoid: Ellipsoid1 | None = field(
        default=None,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_datum: TemporalDatum1 | None = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_datum: VerticalDatum1 | None = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_datum: ImageDatum1 | None = field(
        default=None,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_datum: EngineeringDatum1 | None = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_datum: GeodeticDatum1 | None = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    oblique_cartesian_cs: ObliqueCartesianCs | None = field(
        default=None,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    affine_cs: AffineCs1 | None = field(
        default=None,
        metadata={
            "name": "AffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cylindrical_cs: CylindricalCs | None = field(
        default=None,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polar_cs: PolarCs | None = field(
        default=None,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    spherical_cs: SphericalCs1 | None = field(
        default=None,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    user_defined_cs: UserDefinedCs | None = field(
        default=None,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_cs: LinearCs | None = field(
        default=None,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_cs: TemporalCs | None = field(
        default=None,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_cs: TimeCs1 | None = field(
        default=None,
        metadata={
            "name": "TimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_cs: VerticalCs1 | None = field(
        default=None,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cartesian_cs: CartesianCs1 | None = field(
        default=None,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoidal_cs: EllipsoidalCs1 | None = field(
        default=None,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinate_system_axis: CoordinateSystemAxis | None = field(
        default=None,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    compound_crs: CompoundCrs | None = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geocentric_crs: GeocentricCrs | None = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geographic_crs: GeographicCrs | None = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_crs: TemporalCrs | None = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_crs: ImageCrs | None = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_crs: EngineeringCrs | None = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_crs: VerticalCrs | None = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_crs: GeodeticCrs | None = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_crs: DerivedCrs | None = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    projected_crs: ProjectedCrs | None = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conventional_unit: ConventionalUnit | None = field(
        default=None,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_unit: DerivedUnit | None = field(
        default=None,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    base_unit: BaseUnit | None = field(
        default=None,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    unit_definition: UnitDefinition | None = field(
        default=None,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_proxy: DefinitionProxy | None = field(
        default=None,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_collection: DefinitionCollection | None = field(
        default=None,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dictionary: Dictionary | None = field(
        default=None,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition: Definition | None = field(
        default=None,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    array: Array | None = field(
        default=None,
        metadata={
            "name": "Array",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bag: Bag | None = field(
        default=None,
        metadata={
            "name": "Bag",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
