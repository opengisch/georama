from dataclasses import dataclass, field
from typing import Any

from georama.maps.interfaces.opengis.filter_1_1_0.array_type import ValuePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CategoryPropertyType(ValuePropertyType):
    """
    Property whose content is a Category.
    """

    boolean: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    quantity: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    count: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    boolean_list: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    category_list: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    quantity_list: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    count_list: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    category_extent: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    quantity_extent: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    count_extent: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    value_array: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    composite_value: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    generic_meta_data: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    graph_style: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    label_style: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    topology_style: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    geometry_style: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    feature_style: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    style: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    topo_complex: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    topo_solid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    face: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    edge: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    node: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    moving_object_status: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    directed_observation_at_distance: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    directed_observation: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    observation: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    rectified_grid_coverage: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    grid_coverage: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid_coverage: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_surface_coverage: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve_coverage: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_point_coverage: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    feature_collection: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_topology_complex: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_edge: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_node: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_period: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_instant: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_line_string: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_polygon: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_solid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_curve: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_point: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    multi_geometry: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    rectified_grid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    grid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    geometric_complex: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ring: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    linear_ring: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    solid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    composite_solid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    orientable_surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    tin: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    triangulated_surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    polyhedral_surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    composite_surface: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    polygon: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    orientable_curve: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    curve: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    composite_curve: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    line_string: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    point: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_calendar_era: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_clock: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_calendar: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_ordinal_reference_system: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    time_coordinate_system: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    operation_parameter_group: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    operation_parameter: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    operation_method: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    transformation: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    conversion: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    pass_through_operation: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    concatenated_operation: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ellipsoid: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    prime_meridian: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    geodetic_datum: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    temporal_datum: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    vertical_datum: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    image_datum: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    engineering_datum: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    oblique_cartesian_cs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    cylindrical_cs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    polar_cs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    spherical_cs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    user_defined_cs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    linear_cs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    temporal_cs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    vertical_cs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    cartesian_cs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    ellipsoidal_cs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    coordinate_system_axis: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    compound_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    temporal_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    image_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    engineering_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    derived_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    projected_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    geocentric_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    vertical_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    geographic_crs: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    conventional_unit: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    derived_unit: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    base_unit: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    unit_definition: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    definition_proxy: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    definition_collection: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    dictionary: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    definition: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    array: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    bag: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    null: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
