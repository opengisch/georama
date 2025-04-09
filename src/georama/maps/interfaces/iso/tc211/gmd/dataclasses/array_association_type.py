from dataclasses import dataclass, field
from typing import List, Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_feature_type import (
    AbstractFeatureType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_operation_parameter_property_type import (
    OperationParameterGroup,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_parameter_value_property_type import (
    ParameterValueGroup,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_gmltype import (
    AbstractGmltype,
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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.direction import Direction
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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.measure_type import MeasureType
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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue
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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.valid_time import ValidTime
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.value_array_property_type import (
    CompositeValue,
    ValueArray,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vertical_cs_1 import VerticalCs1

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ArrayAssociationType:
    parameter_value_group: List[ParameterValueGroup] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValueGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    parameter_value: List[ParameterValue1] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_function: List[GridFunction] = field(
        default_factory=list,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coverage_mapping_rule: List[CoverageMappingRule] = field(
        default_factory=list,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coverage_function: List[CoverageFunction] = field(
        default_factory=list,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    file: List[File] = field(
        default_factory=list,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    data_block: List[DataBlock] = field(
        default_factory=list,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_extent: List[QuantityExtent] = field(
        default_factory=list,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_extent: List[CountExtent] = field(
        default_factory=list,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_extent: List[CategoryExtent] = field(
        default_factory=list,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_array: List[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_value: List[CompositeValue] = field(
        default_factory=list,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity_list: List[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    count_list: List[CountList] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    category_list: List[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_list: List[BooleanList] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    quantity: List[Quantity] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    count: List[Count] = field(
        default_factory=list,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    category: List[Category] = field(
        default_factory=list,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    boolean: List[Boolean1] = field(
        default_factory=list,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    shell: List[Shell] = field(
        default_factory=list,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    affine_placement: List[AffinePlacement] = field(
        default_factory=list,
        metadata={
            "name": "AffinePlacement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodesic: List[Geodesic] = field(
        default_factory=list,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodesic_string: List[GeodesicString] = field(
        default_factory=list,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    clothoid: List[Clothoid] = field(
        default_factory=list,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    offset_curve: List[OffsetCurve] = field(
        default_factory=list,
        metadata={
            "name": "OffsetCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bezier: List[Bezier] = field(
        default_factory=list,
        metadata={
            "name": "Bezier",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bspline: List[Bspline] = field(
        default_factory=list,
        metadata={
            "name": "BSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cubic_spline: List[CubicSpline] = field(
        default_factory=list,
        metadata={
            "name": "CubicSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    circle_by_center_point: List[CircleByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_by_center_point: List[ArcByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_by_bulge: List[ArcByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_string_by_bulge: List[ArcStringByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcStringByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    circle: List[Circle] = field(
        default_factory=list,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc: List[Arc] = field(
        default_factory=list,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_string: List[ArcString] = field(
        default_factory=list,
        metadata={
            "name": "ArcString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string_segment: List[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ring: List[Ring] = field(
        default_factory=list,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_ring: List[LinearRing] = field(
        default_factory=list,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope_with_time_period: List[EnvelopeWithTimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope: List[Envelope] = field(
        default_factory=list,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    generic_meta_data: List[GenericMetaData] = field(
        default_factory=list,
        metadata={
            "name": "GenericMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_complex: List[TopoComplex] = field(
        default_factory=list,
        metadata={
            "name": "TopoComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_solid: List[TopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    face: List[Face] = field(
        default_factory=list,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    edge: List[Edge] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    node: List[Node] = field(
        default_factory=list,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    moving_object_status: List[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation_at_distance: List["DirectedObservationAtDistance"] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    directed_observation: List["DirectedObservation"] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    observation: List["Observation"] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid_coverage: List[RectifiedGridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_coverage: List[GridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid_coverage: List[MultiSolidCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface_coverage: List[MultiSurfaceCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve_coverage: List[MultiCurveCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point_coverage: List[MultiPointCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dynamic_feature_collection: List[DynamicFeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dynamic_feature: List[DynamicFeature] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    feature_collection: List["FeatureCollection"] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_topology_complex: List[TimeTopologyComplex] = field(
        default_factory=list,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_edge: List[TimeEdge] = field(
        default_factory=list,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_node: List[TimeNode] = field(
        default_factory=list,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_period: List[TimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_instant: List[TimeInstant] = field(
        default_factory=list,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    rectified_grid: List[RectifiedGrid] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid: List[Grid] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geometric_complex: List[GeometricComplex] = field(
        default_factory=list,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_solid: List[MultiSolid] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_surface: List[MultiSurface] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_curve: List[MultiCurve] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_point: List[MultiPoint] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    multi_geometry: List[MultiGeometry] = field(
        default_factory=list,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_solid: List[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    solid: List[Solid] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_surface: List[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_surface: List[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    tin: List[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    triangulated_surface: List[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polyhedral_surface: List[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    surface: List[Surface] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polygon: List[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    composite_curve: List[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    orientable_curve: List[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    curve: List[Curve] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string: List[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    point: List[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_ordinal_reference_system: List[TimeOrdinalReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_clock: List[TimeClock] = field(
        default_factory=list,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_calendar: List[TimeCalendar] = field(
        default_factory=list,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_coordinate_system: List[TimeCoordinateSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_reference_system: List[TimeReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter_group: List[OperationParameterGroup] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter: List[OperationParameter1] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_method: List[OperationMethod] = field(
        default_factory=list,
        metadata={
            "name": "OperationMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    concatenated_operation: List[ConcatenatedOperation] = field(
        default_factory=list,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    pass_through_operation: List[PassThroughOperation] = field(
        default_factory=list,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    transformation: List[Transformation] = field(
        default_factory=list,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conversion: List[Conversion1] = field(
        default_factory=list,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    prime_meridian: List[PrimeMeridian1] = field(
        default_factory=list,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoid: List[Ellipsoid1] = field(
        default_factory=list,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_datum: List[TemporalDatum1] = field(
        default_factory=list,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_datum: List[VerticalDatum1] = field(
        default_factory=list,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_datum: List[ImageDatum1] = field(
        default_factory=list,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_datum: List[EngineeringDatum1] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_datum: List[GeodeticDatum1] = field(
        default_factory=list,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    oblique_cartesian_cs: List[ObliqueCartesianCs] = field(
        default_factory=list,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    affine_cs: List[AffineCs1] = field(
        default_factory=list,
        metadata={
            "name": "AffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cylindrical_cs: List[CylindricalCs] = field(
        default_factory=list,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    polar_cs: List[PolarCs] = field(
        default_factory=list,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    spherical_cs: List[SphericalCs1] = field(
        default_factory=list,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    user_defined_cs: List[UserDefinedCs] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    linear_cs: List[LinearCs] = field(
        default_factory=list,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_cs: List[TemporalCs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_cs: List[TimeCs1] = field(
        default_factory=list,
        metadata={
            "name": "TimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_cs: List[VerticalCs1] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cartesian_cs: List[CartesianCs1] = field(
        default_factory=list,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoidal_cs: List[EllipsoidalCs1] = field(
        default_factory=list,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coordinate_system_axis: List[CoordinateSystemAxis] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    compound_crs: List[CompoundCrs] = field(
        default_factory=list,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geocentric_crs: List[GeocentricCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geographic_crs: List[GeographicCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_crs: List[TemporalCrs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_crs: List[ImageCrs] = field(
        default_factory=list,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_crs: List[EngineeringCrs] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_crs: List[VerticalCrs] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_crs: List[GeodeticCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_crs: List[DerivedCrs] = field(
        default_factory=list,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    projected_crs: List[ProjectedCrs] = field(
        default_factory=list,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    conventional_unit: List[ConventionalUnit] = field(
        default_factory=list,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    derived_unit: List[DerivedUnit] = field(
        default_factory=list,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    base_unit: List[BaseUnit] = field(
        default_factory=list,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    unit_definition: List[UnitDefinition] = field(
        default_factory=list,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_proxy: List[DefinitionProxy] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition_collection: List[DefinitionCollection] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dictionary: List[Dictionary] = field(
        default_factory=list,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    definition: List[Definition] = field(
        default_factory=list,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    array: List["Array"] = field(
        default_factory=list,
        metadata={
            "name": "Array",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bag: List["Bag"] = field(
        default_factory=list,
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


@dataclass
class AssociationRoleType:
    parameter_value_group: Optional[ParameterValueGroup] = field(
        default=None,
        metadata={
            "name": "ParameterValueGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    parameter_value: Optional[ParameterValue1] = field(
        default=None,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_function: Optional[GridFunction] = field(
        default=None,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coverage_mapping_rule: Optional[CoverageMappingRule] = field(
        default=None,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coverage_function: Optional[CoverageFunction] = field(
        default=None,
        metadata={
            "name": "coverageFunction",
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
    data_block: Optional[DataBlock] = field(
        default=None,
        metadata={
            "name": "DataBlock",
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
    category_extent: Optional[CategoryExtent] = field(
        default=None,
        metadata={
            "name": "CategoryExtent",
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
    category_list: Optional[CategoryList] = field(
        default=None,
        metadata={
            "name": "CategoryList",
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
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    count: Optional[Count] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    category: Optional[Category] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    boolean: Optional[Boolean1] = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    shell: Optional[Shell] = field(
        default=None,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    affine_placement: Optional[AffinePlacement] = field(
        default=None,
        metadata={
            "name": "AffinePlacement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodesic: Optional[Geodesic] = field(
        default=None,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodesic_string: Optional[GeodesicString] = field(
        default=None,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    clothoid: Optional[Clothoid] = field(
        default=None,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    offset_curve: Optional[OffsetCurve] = field(
        default=None,
        metadata={
            "name": "OffsetCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bezier: Optional[Bezier] = field(
        default=None,
        metadata={
            "name": "Bezier",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bspline: Optional[Bspline] = field(
        default=None,
        metadata={
            "name": "BSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cubic_spline: Optional[CubicSpline] = field(
        default=None,
        metadata={
            "name": "CubicSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    circle_by_center_point: Optional[CircleByCenterPoint] = field(
        default=None,
        metadata={
            "name": "CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_by_center_point: Optional[ArcByCenterPoint] = field(
        default=None,
        metadata={
            "name": "ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_by_bulge: Optional[ArcByBulge] = field(
        default=None,
        metadata={
            "name": "ArcByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_string_by_bulge: Optional[ArcStringByBulge] = field(
        default=None,
        metadata={
            "name": "ArcStringByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    circle: Optional[Circle] = field(
        default=None,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc: Optional[Arc] = field(
        default=None,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_string: Optional[ArcString] = field(
        default=None,
        metadata={
            "name": "ArcString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string_segment: Optional[LineStringSegment] = field(
        default=None,
        metadata={
            "name": "LineStringSegment",
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
    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
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
    dynamic_feature_collection: Optional[DynamicFeatureCollection] = field(
        default=None,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dynamic_feature: Optional[DynamicFeature] = field(
        default=None,
        metadata={
            "name": "DynamicFeature",
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
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
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
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
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
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
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
    time_ordinal_reference_system: Optional[TimeOrdinalReferenceSystem] = field(
        default=None,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
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
    time_coordinate_system: Optional[TimeCoordinateSystem] = field(
        default=None,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_reference_system: Optional[TimeReferenceSystem] = field(
        default=None,
        metadata={
            "name": "TimeReferenceSystem",
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
    operation_parameter: Optional[OperationParameter1] = field(
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
    concatenated_operation: Optional[ConcatenatedOperation] = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
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
    prime_meridian: Optional[PrimeMeridian1] = field(
        default=None,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoid: Optional[Ellipsoid1] = field(
        default=None,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_datum: Optional[TemporalDatum1] = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_datum: Optional[VerticalDatum1] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_datum: Optional[ImageDatum1] = field(
        default=None,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_datum: Optional[EngineeringDatum1] = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_datum: Optional[GeodeticDatum1] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
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
    affine_cs: Optional[AffineCs1] = field(
        default=None,
        metadata={
            "name": "AffineCS",
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
    spherical_cs: Optional[SphericalCs1] = field(
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
    time_cs: Optional[TimeCs1] = field(
        default=None,
        metadata={
            "name": "TimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_cs: Optional[VerticalCs1] = field(
        default=None,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cartesian_cs: Optional[CartesianCs1] = field(
        default=None,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoidal_cs: Optional[EllipsoidalCs1] = field(
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
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
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
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
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
    array: Optional["Array"] = field(
        default=None,
        metadata={
            "name": "Array",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bag: Optional["Bag"] = field(
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
class FeatureArrayPropertyType:
    directed_observation_at_distance: List["DirectedObservationAtDistance"] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    directed_observation: List["DirectedObservation"] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    observation: List["Observation"] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    rectified_grid_coverage: List[RectifiedGridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    grid_coverage: List[GridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    multi_solid_coverage: List[MultiSolidCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    multi_surface_coverage: List[MultiSurfaceCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    multi_curve_coverage: List[MultiCurveCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    multi_point_coverage: List[MultiPointCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    dynamic_feature_collection: List[DynamicFeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    dynamic_feature: List[DynamicFeature] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )
    feature_collection: List["FeatureCollection"] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "sequence": 1,
        },
    )


@dataclass
class FeaturePropertyType:
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
    dynamic_feature_collection: Optional[DynamicFeatureCollection] = field(
        default=None,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dynamic_feature: Optional[DynamicFeature] = field(
        default=None,
        metadata={
            "name": "DynamicFeature",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
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
    using: Optional["Using"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    subject: Optional["Subject"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    target: Optional["Target"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    result_of: Optional["ResultOf"] = field(
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
    """The content model is a straightforward extension of gml:AbstractFeatureType;
    it automatically has the gml:identifier, gml:description,
    gml:descriptionReference, gml:name, and gml:boundedBy properties.

    The gml:validTime element describes the time of the observation.
    Note that this may be a time instant or a time period. The gml:using
    property contains or references a description of a sensor,
    instrument or procedure used for the observation. The gml:target
    property contains or references the specimen, region or station
    which is the object of the observation. This property is
    particularly useful for remote observations, such as photographs,
    where a generic location property might apply to the location of the
    camera or the location of the field of view, and thus may be
    ambiguous. The gml:subject element is provided as a convenient
    synonym for gml:target. This is the term commonly used in
    phtotography. The gml:resultOf property indicates the result of the
    observation.  The value may be inline, or a reference to a value
    elsewhere. If the value is inline, it shall be a member of the
    gml:AbstractObject substitution group.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeatureMember(FeaturePropertyType):
    class Meta:
        name = "featureMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeatureMembers(FeatureArrayPropertyType):
    class Meta:
        name = "featureMembers"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Member(AssociationRoleType):
    class Meta:
        name = "member"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Members(ArrayAssociationType):
    class Meta:
        name = "members"
        namespace = "http://www.opengis.net/gml"


@dataclass
class AbstractFeatureCollectionType(AbstractFeatureType):
    feature_member: List[FeatureMember] = field(
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
class ArrayType(AbstractGmltype):
    members: Optional[Members] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class BagType(AbstractGmltype):
    member: List[Member] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    members: Optional[Members] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class DirectedObservation(DirectedObservationType):
    """A gml:DirectedObservation is the same as an observation except that it adds
    an additional gml:direction property.

    This is the direction in which the observation was acquired. Clearly
    this applies only to certain types of observations such as visual
    observations by people, or observations obtained from terrestrial
    cameras.
    """

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
class Array(ArrayType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Bag(BagType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class DirectedObservationAtDistance(DirectedObservationAtDistanceType):
    """Gml:DirectedObservationAtDistance adds an additional distance property.

    This is the distance from the observer to the subject of the
    observation. Clearly this applies only to certain types of
    observations such as visual observations by people, or observations
    obtained from terrestrial cameras.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class FeatureCollectionType(AbstractFeatureCollectionType):
    pass


@dataclass
class FeatureCollection(FeatureCollectionType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class ProcedurePropertyType:
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
    dynamic_feature_collection: Optional[DynamicFeatureCollection] = field(
        default=None,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dynamic_feature: Optional[DynamicFeature] = field(
        default=None,
        metadata={
            "name": "DynamicFeature",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
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
class ResultType:
    parameter_value_group: Optional[ParameterValueGroup] = field(
        default=None,
        metadata={
            "name": "ParameterValueGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    parameter_value: Optional[ParameterValue1] = field(
        default=None,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    grid_function: Optional[GridFunction] = field(
        default=None,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coverage_mapping_rule: Optional[CoverageMappingRule] = field(
        default=None,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    coverage_function: Optional[CoverageFunction] = field(
        default=None,
        metadata={
            "name": "coverageFunction",
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
    data_block: Optional[DataBlock] = field(
        default=None,
        metadata={
            "name": "DataBlock",
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
    category_extent: Optional[CategoryExtent] = field(
        default=None,
        metadata={
            "name": "CategoryExtent",
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
    category_list: Optional[CategoryList] = field(
        default=None,
        metadata={
            "name": "CategoryList",
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
    quantity: Optional[Quantity] = field(
        default=None,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    count: Optional[Count] = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    category: Optional[Category] = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    boolean: Optional[Boolean1] = field(
        default=None,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "nillable": True,
        },
    )
    shell: Optional[Shell] = field(
        default=None,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    affine_placement: Optional[AffinePlacement] = field(
        default=None,
        metadata={
            "name": "AffinePlacement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodesic: Optional[Geodesic] = field(
        default=None,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodesic_string: Optional[GeodesicString] = field(
        default=None,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    clothoid: Optional[Clothoid] = field(
        default=None,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    offset_curve: Optional[OffsetCurve] = field(
        default=None,
        metadata={
            "name": "OffsetCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bezier: Optional[Bezier] = field(
        default=None,
        metadata={
            "name": "Bezier",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    bspline: Optional[Bspline] = field(
        default=None,
        metadata={
            "name": "BSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cubic_spline: Optional[CubicSpline] = field(
        default=None,
        metadata={
            "name": "CubicSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    circle_by_center_point: Optional[CircleByCenterPoint] = field(
        default=None,
        metadata={
            "name": "CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_by_center_point: Optional[ArcByCenterPoint] = field(
        default=None,
        metadata={
            "name": "ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_by_bulge: Optional[ArcByBulge] = field(
        default=None,
        metadata={
            "name": "ArcByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_string_by_bulge: Optional[ArcStringByBulge] = field(
        default=None,
        metadata={
            "name": "ArcStringByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    circle: Optional[Circle] = field(
        default=None,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc: Optional[Arc] = field(
        default=None,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    arc_string: Optional[ArcString] = field(
        default=None,
        metadata={
            "name": "ArcString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    line_string_segment: Optional[LineStringSegment] = field(
        default=None,
        metadata={
            "name": "LineStringSegment",
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
    envelope_with_time_period: Optional[EnvelopeWithTimePeriod] = field(
        default=None,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    envelope: Optional[Envelope] = field(
        default=None,
        metadata={
            "name": "Envelope",
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
    dynamic_feature_collection: Optional[DynamicFeatureCollection] = field(
        default=None,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dynamic_feature: Optional[DynamicFeature] = field(
        default=None,
        metadata={
            "name": "DynamicFeature",
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
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
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
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
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
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
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
    time_ordinal_reference_system: Optional[TimeOrdinalReferenceSystem] = field(
        default=None,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
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
    time_coordinate_system: Optional[TimeCoordinateSystem] = field(
        default=None,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    time_reference_system: Optional[TimeReferenceSystem] = field(
        default=None,
        metadata={
            "name": "TimeReferenceSystem",
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
    operation_parameter: Optional[OperationParameter1] = field(
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
    concatenated_operation: Optional[ConcatenatedOperation] = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
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
    prime_meridian: Optional[PrimeMeridian1] = field(
        default=None,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoid: Optional[Ellipsoid1] = field(
        default=None,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    temporal_datum: Optional[TemporalDatum1] = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_datum: Optional[VerticalDatum1] = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    image_datum: Optional[ImageDatum1] = field(
        default=None,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    engineering_datum: Optional[EngineeringDatum1] = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_datum: Optional[GeodeticDatum1] = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
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
    affine_cs: Optional[AffineCs1] = field(
        default=None,
        metadata={
            "name": "AffineCS",
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
    spherical_cs: Optional[SphericalCs1] = field(
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
    time_cs: Optional[TimeCs1] = field(
        default=None,
        metadata={
            "name": "TimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    vertical_cs: Optional[VerticalCs1] = field(
        default=None,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    cartesian_cs: Optional[CartesianCs1] = field(
        default=None,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    ellipsoidal_cs: Optional[EllipsoidalCs1] = field(
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
    geocentric_crs: Optional[GeocentricCrs] = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
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
    vertical_crs: Optional[VerticalCrs] = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    geodetic_crs: Optional[GeodeticCrs] = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
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
class TargetPropertyType:
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
    dynamic_feature_collection: Optional[DynamicFeatureCollection] = field(
        default=None,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dynamic_feature: Optional[DynamicFeature] = field(
        default=None,
        metadata={
            "name": "DynamicFeature",
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
    composite_solid: Optional[CompositeSolid] = field(
        default=None,
        metadata={
            "name": "CompositeSolid",
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
    composite_surface: Optional[CompositeSurface] = field(
        default=None,
        metadata={
            "name": "CompositeSurface",
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
    polygon: Optional[Polygon] = field(
        default=None,
        metadata={
            "name": "Polygon",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
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
class ResultOf(ResultType):
    class Meta:
        name = "resultOf"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Subject(TargetPropertyType):
    class Meta:
        name = "subject"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Target(TargetPropertyType):
    class Meta:
        name = "target"
        namespace = "http://www.opengis.net/gml"


@dataclass
class Using(ProcedurePropertyType):
    class Meta:
        name = "using"
        namespace = "http://www.opengis.net/gml"
