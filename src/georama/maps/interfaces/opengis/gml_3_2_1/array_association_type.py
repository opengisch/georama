from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_crstype import (
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
from georama.maps.interfaces.opengis.gml_3_2_1.abstract_general_operation_parameter_property_type import (
    OperationParameterGroup,
)
from georama.maps.interfaces.opengis.gml_3_2_1.abstract_general_parameter_value_property_type import (
    ParameterValueGroup,
)
from georama.maps.interfaces.opengis.gml_3_2_1.abstract_gmltype import AbstractGmltype
from georama.maps.interfaces.opengis.gml_3_2_1.abstract_time_primitive_type import (
    TimeEdge,
    TimeInstant,
    TimeNode,
    TimePeriod,
)
from georama.maps.interfaces.opengis.gml_3_2_1.affine_cs_1 import AffineCs1
from georama.maps.interfaces.opengis.gml_3_2_1.affine_placement import AffinePlacement
from georama.maps.interfaces.opengis.gml_3_2_1.arc import Arc
from georama.maps.interfaces.opengis.gml_3_2_1.arc_by_bulge import ArcByBulge
from georama.maps.interfaces.opengis.gml_3_2_1.arc_by_center_point import (
    ArcByCenterPoint,
)
from georama.maps.interfaces.opengis.gml_3_2_1.arc_string import ArcString
from georama.maps.interfaces.opengis.gml_3_2_1.arc_string_by_bulge import (
    ArcStringByBulge,
)
from georama.maps.interfaces.opengis.gml_3_2_1.base_unit import BaseUnit
from georama.maps.interfaces.opengis.gml_3_2_1.bezier import Bezier
from georama.maps.interfaces.opengis.gml_3_2_1.boolean_1 import Boolean1
from georama.maps.interfaces.opengis.gml_3_2_1.boolean_list import BooleanList
from georama.maps.interfaces.opengis.gml_3_2_1.bspline import Bspline
from georama.maps.interfaces.opengis.gml_3_2_1.cartesian_cs_1 import CartesianCs1
from georama.maps.interfaces.opengis.gml_3_2_1.category import Category
from georama.maps.interfaces.opengis.gml_3_2_1.category_extent import CategoryExtent
from georama.maps.interfaces.opengis.gml_3_2_1.category_list import CategoryList
from georama.maps.interfaces.opengis.gml_3_2_1.circle import Circle
from georama.maps.interfaces.opengis.gml_3_2_1.circle_by_center_point import (
    CircleByCenterPoint,
)
from georama.maps.interfaces.opengis.gml_3_2_1.clothoid import Clothoid
from georama.maps.interfaces.opengis.gml_3_2_1.conventional_unit import ConventionalUnit
from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_operation_property_type import (
    ConcatenatedOperation,
    PassThroughOperation,
)
from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_system_axis import (
    CoordinateSystemAxis,
)
from georama.maps.interfaces.opengis.gml_3_2_1.count import Count
from georama.maps.interfaces.opengis.gml_3_2_1.count_extent import CountExtent
from georama.maps.interfaces.opengis.gml_3_2_1.count_list import CountList
from georama.maps.interfaces.opengis.gml_3_2_1.coverage_function import CoverageFunction
from georama.maps.interfaces.opengis.gml_3_2_1.coverage_mapping_rule import (
    CoverageMappingRule,
)
from georama.maps.interfaces.opengis.gml_3_2_1.cubic_spline import CubicSpline
from georama.maps.interfaces.opengis.gml_3_2_1.curve_property_type import (
    CompositeCurve,
    Curve,
    OffsetCurve,
    OrientableCurve,
    Ring,
)
from georama.maps.interfaces.opengis.gml_3_2_1.cylindrical_cs_1 import CylindricalCs1
from georama.maps.interfaces.opengis.gml_3_2_1.data_block import DataBlock
from georama.maps.interfaces.opengis.gml_3_2_1.definition import Definition
from georama.maps.interfaces.opengis.gml_3_2_1.definition_proxy import DefinitionProxy
from georama.maps.interfaces.opengis.gml_3_2_1.derived_unit import DerivedUnit
from georama.maps.interfaces.opengis.gml_3_2_1.dictionary_type import (
    DefinitionCollection,
    Dictionary,
)
from georama.maps.interfaces.opengis.gml_3_2_1.dynamic_feature import DynamicFeature
from georama.maps.interfaces.opengis.gml_3_2_1.dynamic_feature_collection_type import (
    DynamicFeatureCollection,
)
from georama.maps.interfaces.opengis.gml_3_2_1.ellipsoid_1 import Ellipsoid1
from georama.maps.interfaces.opengis.gml_3_2_1.ellipsoidal_cs_1 import EllipsoidalCs1
from georama.maps.interfaces.opengis.gml_3_2_1.envelope import Envelope
from georama.maps.interfaces.opengis.gml_3_2_1.envelope_with_time_period import (
    EnvelopeWithTimePeriod,
)
from georama.maps.interfaces.opengis.gml_3_2_1.face_or_topo_solid_property_type import (
    Edge,
    Face,
    Node,
    TopoSolid,
)
from georama.maps.interfaces.opengis.gml_3_2_1.feature_property_type import (
    DirectedObservation,
    DirectedObservationAtDistance,
    FeatureCollection,
    Observation,
)
from georama.maps.interfaces.opengis.gml_3_2_1.file import File
from georama.maps.interfaces.opengis.gml_3_2_1.generic_meta_data import GenericMetaData
from georama.maps.interfaces.opengis.gml_3_2_1.geodesic import Geodesic
from georama.maps.interfaces.opengis.gml_3_2_1.geodesic_string import GeodesicString
from georama.maps.interfaces.opengis.gml_3_2_1.geometric_complex import GeometricComplex
from georama.maps.interfaces.opengis.gml_3_2_1.geometry_array_property_type import (
    MultiGeometry,
)
from georama.maps.interfaces.opengis.gml_3_2_1.grid import Grid
from georama.maps.interfaces.opengis.gml_3_2_1.grid_coverage import GridCoverage
from georama.maps.interfaces.opengis.gml_3_2_1.grid_function import GridFunction
from georama.maps.interfaces.opengis.gml_3_2_1.line_string import LineString
from georama.maps.interfaces.opengis.gml_3_2_1.line_string_segment import (
    LineStringSegment,
)
from georama.maps.interfaces.opengis.gml_3_2_1.linear_cs_1 import LinearCs1
from georama.maps.interfaces.opengis.gml_3_2_1.linear_ring import LinearRing
from georama.maps.interfaces.opengis.gml_3_2_1.member import Member
from georama.maps.interfaces.opengis.gml_3_2_1.moving_object_status import (
    MovingObjectStatus,
)
from georama.maps.interfaces.opengis.gml_3_2_1.multi_curve import MultiCurve
from georama.maps.interfaces.opengis.gml_3_2_1.multi_curve_coverage import (
    MultiCurveCoverage,
)
from georama.maps.interfaces.opengis.gml_3_2_1.multi_point import MultiPoint
from georama.maps.interfaces.opengis.gml_3_2_1.multi_point_coverage import (
    MultiPointCoverage,
)
from georama.maps.interfaces.opengis.gml_3_2_1.multi_solid import MultiSolid
from georama.maps.interfaces.opengis.gml_3_2_1.multi_solid_coverage import (
    MultiSolidCoverage,
)
from georama.maps.interfaces.opengis.gml_3_2_1.multi_surface import MultiSurface
from georama.maps.interfaces.opengis.gml_3_2_1.multi_surface_coverage import (
    MultiSurfaceCoverage,
)
from georama.maps.interfaces.opengis.gml_3_2_1.oblique_cartesian_cs import (
    ObliqueCartesianCs,
)
from georama.maps.interfaces.opengis.gml_3_2_1.operation_method import OperationMethod
from georama.maps.interfaces.opengis.gml_3_2_1.operation_parameter_1 import (
    OperationParameter1,
)
from georama.maps.interfaces.opengis.gml_3_2_1.parameter_value_1 import ParameterValue1
from georama.maps.interfaces.opengis.gml_3_2_1.point import Point
from georama.maps.interfaces.opengis.gml_3_2_1.polar_cs_1 import PolarCs1
from georama.maps.interfaces.opengis.gml_3_2_1.polygon import Polygon
from georama.maps.interfaces.opengis.gml_3_2_1.polyhedral_surface import (
    PolyhedralSurface,
)
from georama.maps.interfaces.opengis.gml_3_2_1.prime_meridian_1 import PrimeMeridian1
from georama.maps.interfaces.opengis.gml_3_2_1.quantity import Quantity
from georama.maps.interfaces.opengis.gml_3_2_1.quantity_extent import QuantityExtent
from georama.maps.interfaces.opengis.gml_3_2_1.quantity_list import QuantityList
from georama.maps.interfaces.opengis.gml_3_2_1.rectified_grid import RectifiedGrid
from georama.maps.interfaces.opengis.gml_3_2_1.rectified_grid_coverage import (
    RectifiedGridCoverage,
)
from georama.maps.interfaces.opengis.gml_3_2_1.solid import Solid
from georama.maps.interfaces.opengis.gml_3_2_1.solid_property_type import CompositeSolid
from georama.maps.interfaces.opengis.gml_3_2_1.spherical_cs_1 import SphericalCs1
from georama.maps.interfaces.opengis.gml_3_2_1.surface import Surface
from georama.maps.interfaces.opengis.gml_3_2_1.surface_property_type import (
    CompositeSurface,
    OrientableSurface,
    Shell,
)
from georama.maps.interfaces.opengis.gml_3_2_1.temporal_cs import TemporalCs
from georama.maps.interfaces.opengis.gml_3_2_1.time_calendar import TimeCalendar
from georama.maps.interfaces.opengis.gml_3_2_1.time_clock import TimeClock
from georama.maps.interfaces.opengis.gml_3_2_1.time_coordinate_system import (
    TimeCoordinateSystem,
)
from georama.maps.interfaces.opengis.gml_3_2_1.time_cs_1 import TimeCs1
from georama.maps.interfaces.opengis.gml_3_2_1.time_ordinal_reference_system import (
    TimeOrdinalReferenceSystem,
)
from georama.maps.interfaces.opengis.gml_3_2_1.time_reference_system import (
    TimeReferenceSystem,
)
from georama.maps.interfaces.opengis.gml_3_2_1.time_topology_complex import (
    TimeTopologyComplex,
)
from georama.maps.interfaces.opengis.gml_3_2_1.tin import Tin
from georama.maps.interfaces.opengis.gml_3_2_1.topo_complex_type import TopoComplex
from georama.maps.interfaces.opengis.gml_3_2_1.transformation import Transformation
from georama.maps.interfaces.opengis.gml_3_2_1.triangulated_surface import (
    TriangulatedSurface,
)
from georama.maps.interfaces.opengis.gml_3_2_1.unit_definition import UnitDefinition
from georama.maps.interfaces.opengis.gml_3_2_1.user_defined_cs_1 import UserDefinedCs1
from georama.maps.interfaces.opengis.gml_3_2_1.value_array_property_type import (
    CompositeValue,
    ValueArray,
)
from georama.maps.interfaces.opengis.gml_3_2_1.vertical_cs_1 import VerticalCs1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ArrayAssociationType:
    generic_meta_data: list[GenericMetaData] = field(
        default_factory=list,
        metadata={
            "name": "GenericMetaData",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    parameter_value_group: list[ParameterValueGroup] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValueGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    parameter_value: list[ParameterValue1] = field(
        default_factory=list,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_function: list[GridFunction] = field(
        default_factory=list,
        metadata={
            "name": "GridFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coverage_mapping_rule: list[CoverageMappingRule] = field(
        default_factory=list,
        metadata={
            "name": "CoverageMappingRule",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coverage_function: list[CoverageFunction] = field(
        default_factory=list,
        metadata={
            "name": "coverageFunction",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    file: list[File] = field(
        default_factory=list,
        metadata={
            "name": "File",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    data_block: list[DataBlock] = field(
        default_factory=list,
        metadata={
            "name": "DataBlock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    quantity_extent: list[QuantityExtent] = field(
        default_factory=list,
        metadata={
            "name": "QuantityExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    count_extent: list[CountExtent] = field(
        default_factory=list,
        metadata={
            "name": "CountExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    category_extent: list[CategoryExtent] = field(
        default_factory=list,
        metadata={
            "name": "CategoryExtent",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    value_array: list[ValueArray] = field(
        default_factory=list,
        metadata={
            "name": "ValueArray",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_value: list[CompositeValue] = field(
        default_factory=list,
        metadata={
            "name": "CompositeValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    quantity_list: list[QuantityList] = field(
        default_factory=list,
        metadata={
            "name": "QuantityList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    count_list: list[CountList] = field(
        default_factory=list,
        metadata={
            "name": "CountList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    category_list: list[CategoryList] = field(
        default_factory=list,
        metadata={
            "name": "CategoryList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    boolean_list: list[BooleanList] = field(
        default_factory=list,
        metadata={
            "name": "BooleanList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    quantity: list[Quantity] = field(
        default_factory=list,
        metadata={
            "name": "Quantity",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )
    count: list[Count] = field(
        default_factory=list,
        metadata={
            "name": "Count",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )
    category: list[Category] = field(
        default_factory=list,
        metadata={
            "name": "Category",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )
    boolean: list[Boolean1] = field(
        default_factory=list,
        metadata={
            "name": "Boolean",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "nillable": True,
        },
    )
    affine_placement: list[AffinePlacement] = field(
        default_factory=list,
        metadata={
            "name": "AffinePlacement",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodesic: list[Geodesic] = field(
        default_factory=list,
        metadata={
            "name": "Geodesic",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodesic_string: list[GeodesicString] = field(
        default_factory=list,
        metadata={
            "name": "GeodesicString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    clothoid: list[Clothoid] = field(
        default_factory=list,
        metadata={
            "name": "Clothoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    offset_curve: list[OffsetCurve] = field(
        default_factory=list,
        metadata={
            "name": "OffsetCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    bezier: list[Bezier] = field(
        default_factory=list,
        metadata={
            "name": "Bezier",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    bspline: list[Bspline] = field(
        default_factory=list,
        metadata={
            "name": "BSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cubic_spline: list[CubicSpline] = field(
        default_factory=list,
        metadata={
            "name": "CubicSpline",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    circle_by_center_point: list[CircleByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "CircleByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    arc_by_center_point: list[ArcByCenterPoint] = field(
        default_factory=list,
        metadata={
            "name": "ArcByCenterPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    arc_by_bulge: list[ArcByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    arc_string_by_bulge: list[ArcStringByBulge] = field(
        default_factory=list,
        metadata={
            "name": "ArcStringByBulge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    circle: list[Circle] = field(
        default_factory=list,
        metadata={
            "name": "Circle",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    arc: list[Arc] = field(
        default_factory=list,
        metadata={
            "name": "Arc",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    arc_string: list[ArcString] = field(
        default_factory=list,
        metadata={
            "name": "ArcString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    line_string_segment: list[LineStringSegment] = field(
        default_factory=list,
        metadata={
            "name": "LineStringSegment",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    envelope_with_time_period: list[EnvelopeWithTimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "EnvelopeWithTimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    envelope: list[Envelope] = field(
        default_factory=list,
        metadata={
            "name": "Envelope",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    array: list["Array"] = field(
        default_factory=list,
        metadata={
            "name": "Array",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    bag: list["Bag"] = field(
        default_factory=list,
        metadata={
            "name": "Bag",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    topo_complex: list[TopoComplex] = field(
        default_factory=list,
        metadata={
            "name": "TopoComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    topo_solid: list[TopoSolid] = field(
        default_factory=list,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    face: list[Face] = field(
        default_factory=list,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    edge: list[Edge] = field(
        default_factory=list,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    node: list[Node] = field(
        default_factory=list,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    moving_object_status: list[MovingObjectStatus] = field(
        default_factory=list,
        metadata={
            "name": "MovingObjectStatus",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    feature_collection: list[FeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "FeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_observation_at_distance: list[DirectedObservationAtDistance] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservationAtDistance",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_observation: list[DirectedObservation] = field(
        default_factory=list,
        metadata={
            "name": "DirectedObservation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    observation: list[Observation] = field(
        default_factory=list,
        metadata={
            "name": "Observation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rectified_grid_coverage: list[RectifiedGridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid_coverage: list[GridCoverage] = field(
        default_factory=list,
        metadata={
            "name": "GridCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_solid_coverage: list[MultiSolidCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolidCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_surface_coverage: list[MultiSurfaceCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurfaceCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_curve_coverage: list[MultiCurveCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurveCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_point_coverage: list[MultiPointCoverage] = field(
        default_factory=list,
        metadata={
            "name": "MultiPointCoverage",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature_collection: list[DynamicFeatureCollection] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeatureCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dynamic_feature: list[DynamicFeature] = field(
        default_factory=list,
        metadata={
            "name": "DynamicFeature",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_topology_complex: list[TimeTopologyComplex] = field(
        default_factory=list,
        metadata={
            "name": "TimeTopologyComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_edge: list[TimeEdge] = field(
        default_factory=list,
        metadata={
            "name": "TimeEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_node: list[TimeNode] = field(
        default_factory=list,
        metadata={
            "name": "TimeNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_period: list[TimePeriod] = field(
        default_factory=list,
        metadata={
            "name": "TimePeriod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_instant: list[TimeInstant] = field(
        default_factory=list,
        metadata={
            "name": "TimeInstant",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    rectified_grid: list[RectifiedGrid] = field(
        default_factory=list,
        metadata={
            "name": "RectifiedGrid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    grid: list[Grid] = field(
        default_factory=list,
        metadata={
            "name": "Grid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geometric_complex: list[GeometricComplex] = field(
        default_factory=list,
        metadata={
            "name": "GeometricComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_solid: list[MultiSolid] = field(
        default_factory=list,
        metadata={
            "name": "MultiSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_surface: list[MultiSurface] = field(
        default_factory=list,
        metadata={
            "name": "MultiSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_curve: list[MultiCurve] = field(
        default_factory=list,
        metadata={
            "name": "MultiCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_point: list[MultiPoint] = field(
        default_factory=list,
        metadata={
            "name": "MultiPoint",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    multi_geometry: list[MultiGeometry] = field(
        default_factory=list,
        metadata={
            "name": "MultiGeometry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_solid: list[CompositeSolid] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    solid: list[Solid] = field(
        default_factory=list,
        metadata={
            "name": "Solid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_surface: list[CompositeSurface] = field(
        default_factory=list,
        metadata={
            "name": "CompositeSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    shell: list[Shell] = field(
        default_factory=list,
        metadata={
            "name": "Shell",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientable_surface: list[OrientableSurface] = field(
        default_factory=list,
        metadata={
            "name": "OrientableSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    tin: list[Tin] = field(
        default_factory=list,
        metadata={
            "name": "Tin",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    triangulated_surface: list[TriangulatedSurface] = field(
        default_factory=list,
        metadata={
            "name": "TriangulatedSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polyhedral_surface: list[PolyhedralSurface] = field(
        default_factory=list,
        metadata={
            "name": "PolyhedralSurface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    surface: list[Surface] = field(
        default_factory=list,
        metadata={
            "name": "Surface",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polygon: list[Polygon] = field(
        default_factory=list,
        metadata={
            "name": "Polygon",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    composite_curve: list[CompositeCurve] = field(
        default_factory=list,
        metadata={
            "name": "CompositeCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientable_curve: list[OrientableCurve] = field(
        default_factory=list,
        metadata={
            "name": "OrientableCurve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    curve: list[Curve] = field(
        default_factory=list,
        metadata={
            "name": "Curve",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ring: list[Ring] = field(
        default_factory=list,
        metadata={
            "name": "Ring",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    linear_ring: list[LinearRing] = field(
        default_factory=list,
        metadata={
            "name": "LinearRing",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    line_string: list[LineString] = field(
        default_factory=list,
        metadata={
            "name": "LineString",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point: list[Point] = field(
        default_factory=list,
        metadata={
            "name": "Point",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    definition_proxy: list[DefinitionProxy] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    definition_collection: list[DefinitionCollection] = field(
        default_factory=list,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_ordinal_reference_system: list[TimeOrdinalReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_clock: list[TimeClock] = field(
        default_factory=list,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_calendar: list[TimeCalendar] = field(
        default_factory=list,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_coordinate_system: list[TimeCoordinateSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_reference_system: list[TimeReferenceSystem] = field(
        default_factory=list,
        metadata={
            "name": "TimeReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_parameter_group: list[OperationParameterGroup] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_parameter: list[OperationParameter1] = field(
        default_factory=list,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_method: list[OperationMethod] = field(
        default_factory=list,
        metadata={
            "name": "OperationMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    concatenated_operation: list[ConcatenatedOperation] = field(
        default_factory=list,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    transformation: list[Transformation] = field(
        default_factory=list,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    conversion: list[Conversion1] = field(
        default_factory=list,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pass_through_operation: list[PassThroughOperation] = field(
        default_factory=list,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    prime_meridian: list[PrimeMeridian1] = field(
        default_factory=list,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ellipsoid: list[Ellipsoid1] = field(
        default_factory=list,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_datum: list[TemporalDatum1] = field(
        default_factory=list,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_datum: list[VerticalDatum1] = field(
        default_factory=list,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    image_datum: list[ImageDatum1] = field(
        default_factory=list,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    engineering_datum: list[EngineeringDatum1] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodetic_datum: list[GeodeticDatum1] = field(
        default_factory=list,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    oblique_cartesian_cs: list[ObliqueCartesianCs] = field(
        default_factory=list,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_cs: list[TemporalCs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    affine_cs: list[AffineCs1] = field(
        default_factory=list,
        metadata={
            "name": "AffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cylindrical_cs: list[CylindricalCs1] = field(
        default_factory=list,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polar_cs: list[PolarCs1] = field(
        default_factory=list,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    spherical_cs: list[SphericalCs1] = field(
        default_factory=list,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    user_defined_cs: list[UserDefinedCs1] = field(
        default_factory=list,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    linear_cs: list[LinearCs1] = field(
        default_factory=list,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_cs: list[TimeCs1] = field(
        default_factory=list,
        metadata={
            "name": "TimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_cs: list[VerticalCs1] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cartesian_cs: list[CartesianCs1] = field(
        default_factory=list,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ellipsoidal_cs: list[EllipsoidalCs1] = field(
        default_factory=list,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinate_system_axis: list[CoordinateSystemAxis] = field(
        default_factory=list,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    compound_crs: list[CompoundCrs] = field(
        default_factory=list,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geocentric_crs: list[GeocentricCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geographic_crs: list[GeographicCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_crs: list[TemporalCrs] = field(
        default_factory=list,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    image_crs: list[ImageCrs] = field(
        default_factory=list,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    engineering_crs: list[EngineeringCrs] = field(
        default_factory=list,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_crs: list[VerticalCrs] = field(
        default_factory=list,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodetic_crs: list[GeodeticCrs] = field(
        default_factory=list,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derived_crs: list[DerivedCrs] = field(
        default_factory=list,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    projected_crs: list[ProjectedCrs] = field(
        default_factory=list,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    conventional_unit: list[ConventionalUnit] = field(
        default_factory=list,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derived_unit: list[DerivedUnit] = field(
        default_factory=list,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    base_unit: list[BaseUnit] = field(
        default_factory=list,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    unit_definition: list[UnitDefinition] = field(
        default_factory=list,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dictionary: list[Dictionary] = field(
        default_factory=list,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    definition: list[Definition] = field(
        default_factory=list,
        metadata={
            "name": "Definition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Members(ArrayAssociationType):
    class Meta:
        name = "members"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ArrayType(AbstractGmltype):
    members: Optional[Members] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class BagType(AbstractGmltype):
    member: list[Member] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    members: Optional[Members] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class Array(ArrayType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Bag(BagType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
