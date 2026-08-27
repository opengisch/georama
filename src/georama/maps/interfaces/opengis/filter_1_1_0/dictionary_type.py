from dataclasses import dataclass, field
from typing import ForwardRef, Union

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_operation_parameter_ref_type import (
    OperationParameterGroup,
)
from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.base_unit import BaseUnit
from georama.maps.interfaces.opengis.filter_1_1_0.cartesian_cs import CartesianCs
from georama.maps.interfaces.opengis.filter_1_1_0.concatenated_operation import (
    ConcatenatedOperation,
)
from georama.maps.interfaces.opengis.filter_1_1_0.conventional_unit import (
    ConventionalUnit,
)
from georama.maps.interfaces.opengis.filter_1_1_0.coordinate_system_axis import (
    CoordinateSystemAxis,
)
from georama.maps.interfaces.opengis.filter_1_1_0.crsref_type import (
    CompoundCrs,
    Conversion,
    DerivedCrs,
    ProjectedCrs,
)
from georama.maps.interfaces.opengis.filter_1_1_0.cylindrical_cs import CylindricalCs
from georama.maps.interfaces.opengis.filter_1_1_0.definition import Definition
from georama.maps.interfaces.opengis.filter_1_1_0.definition_proxy import (
    DefinitionProxy,
)
from georama.maps.interfaces.opengis.filter_1_1_0.definition_type import DefinitionType
from georama.maps.interfaces.opengis.filter_1_1_0.derived_unit import DerivedUnit
from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoid import Ellipsoid
from georama.maps.interfaces.opengis.filter_1_1_0.ellipsoidal_cs import EllipsoidalCs
from georama.maps.interfaces.opengis.filter_1_1_0.engineering_crs import EngineeringCrs
from georama.maps.interfaces.opengis.filter_1_1_0.engineering_datum import (
    EngineeringDatum,
)
from georama.maps.interfaces.opengis.filter_1_1_0.geocentric_crs import GeocentricCrs
from georama.maps.interfaces.opengis.filter_1_1_0.geodetic_datum import GeodeticDatum
from georama.maps.interfaces.opengis.filter_1_1_0.geographic_crs import GeographicCrs
from georama.maps.interfaces.opengis.filter_1_1_0.image_crs import ImageCrs
from georama.maps.interfaces.opengis.filter_1_1_0.image_datum import ImageDatum
from georama.maps.interfaces.opengis.filter_1_1_0.indirect_entry import IndirectEntry
from georama.maps.interfaces.opengis.filter_1_1_0.linear_cs import LinearCs
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
from georama.maps.interfaces.opengis.filter_1_1_0.polar_cs import PolarCs
from georama.maps.interfaces.opengis.filter_1_1_0.prime_meridian import PrimeMeridian
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.spherical_cs import SphericalCs
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
from georama.maps.interfaces.opengis.filter_1_1_0.transformation import Transformation
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType
from georama.maps.interfaces.opengis.filter_1_1_0.unit_definition import UnitDefinition
from georama.maps.interfaces.opengis.filter_1_1_0.user_defined_cs import UserDefinedCs
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_crs import VerticalCrs
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_cs import VerticalCs
from georama.maps.interfaces.opengis.filter_1_1_0.vertical_datum import VerticalDatum

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DictionaryType(DefinitionType):
    """A non-abstract bag that is specialized for use as a dictionary which
    contains a set of definitions.

    These definitions are referenced from other places, in the same and
    different XML documents. In this restricted type, the inherited
    optional "description" element can be used for a description of this
    dictionary. The inherited optional "name" element can be used for
    the name(s) of this dictionary. The inherited "metaDataProperty"
    elements can be used to reference or contain more information about
    this dictionary. The inherited required gml:id attribute allows the
    dictionary to be referenced using this handle.
    """

    definition_member_or_dictionary_entry_or_indirect_entry: list[
        Union["DefinitionMember", "DictionaryEntry", IndirectEntry]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "definitionMember",
                    "type": ForwardRef("DefinitionMember"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "dictionaryEntry",
                    "type": ForwardRef("DictionaryEntry"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "indirectEntry",
                    "type": IndirectEntry,
                    "namespace": "http://www.opengis.net/gml",
                },
            ),
        },
    )


@dataclass
class DefinitionCollection(DictionaryType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class Dictionary(DictionaryType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class DictionaryEntryType:
    """An entry in a dictionary of definitions.

    An instance of this type contains or refers to a definition object.
    The number of definitions contained in this dictionaryEntry is
    restricted to one, but a DefinitionCollection or Dictionary that
    contains multiple definitions can be substituted if needed.
    Specialized descendents of this dictionaryEntry might be restricted
    in an application schema to allow only including specified types of
    definitions as valid entries in a dictionary.
    """

    choice: (
        TimeCalendarEra
        | TimeClock
        | TimeCalendar
        | TimeOrdinalReferenceSystem
        | TimeCoordinateSystem
        | OperationParameterGroup
        | OperationParameter
        | OperationMethod
        | Transformation
        | Conversion
        | PassThroughOperation
        | ConcatenatedOperation
        | Ellipsoid
        | PrimeMeridian
        | GeodeticDatum
        | TemporalDatum
        | VerticalDatum
        | ImageDatum
        | EngineeringDatum
        | ObliqueCartesianCs
        | CylindricalCs
        | PolarCs
        | SphericalCs
        | UserDefinedCs
        | LinearCs
        | TemporalCs
        | VerticalCs
        | CartesianCs
        | EllipsoidalCs
        | CoordinateSystemAxis
        | CompoundCrs
        | TemporalCrs
        | ImageCrs
        | EngineeringCrs
        | DerivedCrs
        | ProjectedCrs
        | GeocentricCrs
        | VerticalCrs
        | GeographicCrs
        | ConventionalUnit
        | DerivedUnit
        | BaseUnit
        | UnitDefinition
        | DefinitionProxy
        | DefinitionCollection
        | Dictionary
        | Definition
        | None
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
    href: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    role: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    remote_schema: str | None = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class DefinitionMember(DictionaryEntryType):
    class Meta:
        name = "definitionMember"
        namespace = "http://www.opengis.net/gml"


@dataclass
class DictionaryEntry(DictionaryEntryType):
    class Meta:
        name = "dictionaryEntry"
        namespace = "http://www.opengis.net/gml"
