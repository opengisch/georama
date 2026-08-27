from dataclasses import dataclass, field

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
from georama.maps.interfaces.opengis.gml_3_2_1.abstract_member_type import (
    AbstractMemberType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.affine_cs_1 import AffineCs1
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType
from georama.maps.interfaces.opengis.gml_3_2_1.base_unit import BaseUnit
from georama.maps.interfaces.opengis.gml_3_2_1.cartesian_cs_1 import CartesianCs1
from georama.maps.interfaces.opengis.gml_3_2_1.conventional_unit import ConventionalUnit
from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_operation_property_type import (
    ConcatenatedOperation,
    PassThroughOperation,
)
from georama.maps.interfaces.opengis.gml_3_2_1.coordinate_system_axis import (
    CoordinateSystemAxis,
)
from georama.maps.interfaces.opengis.gml_3_2_1.cylindrical_cs_1 import CylindricalCs1
from georama.maps.interfaces.opengis.gml_3_2_1.definition import Definition
from georama.maps.interfaces.opengis.gml_3_2_1.definition_proxy import DefinitionProxy
from georama.maps.interfaces.opengis.gml_3_2_1.definition_type import DefinitionType
from georama.maps.interfaces.opengis.gml_3_2_1.derived_unit import DerivedUnit
from georama.maps.interfaces.opengis.gml_3_2_1.ellipsoid_1 import Ellipsoid1
from georama.maps.interfaces.opengis.gml_3_2_1.ellipsoidal_cs_1 import EllipsoidalCs1
from georama.maps.interfaces.opengis.gml_3_2_1.indirect_entry import IndirectEntry
from georama.maps.interfaces.opengis.gml_3_2_1.linear_cs_1 import LinearCs1
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.oblique_cartesian_cs import (
    ObliqueCartesianCs,
)
from georama.maps.interfaces.opengis.gml_3_2_1.operation_method import OperationMethod
from georama.maps.interfaces.opengis.gml_3_2_1.operation_parameter_1 import (
    OperationParameter1,
)
from georama.maps.interfaces.opengis.gml_3_2_1.polar_cs_1 import PolarCs1
from georama.maps.interfaces.opengis.gml_3_2_1.prime_meridian_1 import PrimeMeridian1
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.spherical_cs_1 import SphericalCs1
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
from georama.maps.interfaces.opengis.gml_3_2_1.transformation import Transformation
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType
from georama.maps.interfaces.opengis.gml_3_2_1.unit_definition import UnitDefinition
from georama.maps.interfaces.opengis.gml_3_2_1.user_defined_cs_1 import UserDefinedCs1
from georama.maps.interfaces.opengis.gml_3_2_1.vertical_cs_1 import VerticalCs1

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class DictionaryType(DefinitionType):
    definition_member: list["DefinitionMember"] = field(
        default_factory=list,
        metadata={
            "name": "definitionMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dictionary_entry: list["DictionaryEntry"] = field(
        default_factory=list,
        metadata={
            "name": "dictionaryEntry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    indirect_entry: list[IndirectEntry] = field(
        default_factory=list,
        metadata={
            "name": "indirectEntry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    aggregation_type: AggregationType | None = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )


@dataclass
class DefinitionCollection(DictionaryType):
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Dictionary(DictionaryType):
    """Sets of definitions may be collected into dictionaries or collections.

    A gml:Dictionary is a non-abstract collection of definitions. The
    gml:Dictionary content model adds a list of gml:dictionaryEntry
    properties that contain or reference gml:Definition objects.  A
    database handle (gml:id attribute) is required, in order that this
    collection may be referred to. The standard gml:identifier,
    gml:description, gml:descriptionReference and gml:name properties
    are available to reference or contain more information about this
    dictionary. The gml:description and gml:descriptionReference
    property elements may be used for a description of this dictionary.
    The derived gml:name element may be used for the name(s) of this
    dictionary. for remote definiton references gml:dictionaryEntry
    shall be used. If a Definition object contained within a Dictionary
    uses the descriptionReference property to refer to a remote
    definition, then this enables the inclusion of a remote definition
    in a local dictionary, giving a handle and identifier in the context
    of the local dictionary.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DictionaryEntryType(AbstractMemberType):
    definition_proxy: DefinitionProxy | None = field(
        default=None,
        metadata={
            "name": "DefinitionProxy",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    definition_collection: DefinitionCollection | None = field(
        default=None,
        metadata={
            "name": "DefinitionCollection",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_ordinal_reference_system: TimeOrdinalReferenceSystem | None = field(
        default=None,
        metadata={
            "name": "TimeOrdinalReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_clock: TimeClock | None = field(
        default=None,
        metadata={
            "name": "TimeClock",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_calendar: TimeCalendar | None = field(
        default=None,
        metadata={
            "name": "TimeCalendar",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_coordinate_system: TimeCoordinateSystem | None = field(
        default=None,
        metadata={
            "name": "TimeCoordinateSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_reference_system: TimeReferenceSystem | None = field(
        default=None,
        metadata={
            "name": "TimeReferenceSystem",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_parameter_group: OperationParameterGroup | None = field(
        default=None,
        metadata={
            "name": "OperationParameterGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_parameter: OperationParameter1 | None = field(
        default=None,
        metadata={
            "name": "OperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_method: OperationMethod | None = field(
        default=None,
        metadata={
            "name": "OperationMethod",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    concatenated_operation: ConcatenatedOperation | None = field(
        default=None,
        metadata={
            "name": "ConcatenatedOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    transformation: Transformation | None = field(
        default=None,
        metadata={
            "name": "Transformation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    conversion: Conversion1 | None = field(
        default=None,
        metadata={
            "name": "Conversion",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    pass_through_operation: PassThroughOperation | None = field(
        default=None,
        metadata={
            "name": "PassThroughOperation",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    prime_meridian: PrimeMeridian1 | None = field(
        default=None,
        metadata={
            "name": "PrimeMeridian",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ellipsoid: Ellipsoid1 | None = field(
        default=None,
        metadata={
            "name": "Ellipsoid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_datum: TemporalDatum1 | None = field(
        default=None,
        metadata={
            "name": "TemporalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_datum: VerticalDatum1 | None = field(
        default=None,
        metadata={
            "name": "VerticalDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    image_datum: ImageDatum1 | None = field(
        default=None,
        metadata={
            "name": "ImageDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    engineering_datum: EngineeringDatum1 | None = field(
        default=None,
        metadata={
            "name": "EngineeringDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodetic_datum: GeodeticDatum1 | None = field(
        default=None,
        metadata={
            "name": "GeodeticDatum",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    oblique_cartesian_cs: ObliqueCartesianCs | None = field(
        default=None,
        metadata={
            "name": "ObliqueCartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_cs: TemporalCs | None = field(
        default=None,
        metadata={
            "name": "TemporalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    affine_cs: AffineCs1 | None = field(
        default=None,
        metadata={
            "name": "AffineCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cylindrical_cs: CylindricalCs1 | None = field(
        default=None,
        metadata={
            "name": "CylindricalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    polar_cs: PolarCs1 | None = field(
        default=None,
        metadata={
            "name": "PolarCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    spherical_cs: SphericalCs1 | None = field(
        default=None,
        metadata={
            "name": "SphericalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    user_defined_cs: UserDefinedCs1 | None = field(
        default=None,
        metadata={
            "name": "UserDefinedCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    linear_cs: LinearCs1 | None = field(
        default=None,
        metadata={
            "name": "LinearCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    time_cs: TimeCs1 | None = field(
        default=None,
        metadata={
            "name": "TimeCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_cs: VerticalCs1 | None = field(
        default=None,
        metadata={
            "name": "VerticalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    cartesian_cs: CartesianCs1 | None = field(
        default=None,
        metadata={
            "name": "CartesianCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    ellipsoidal_cs: EllipsoidalCs1 | None = field(
        default=None,
        metadata={
            "name": "EllipsoidalCS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    coordinate_system_axis: CoordinateSystemAxis | None = field(
        default=None,
        metadata={
            "name": "CoordinateSystemAxis",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    compound_crs: CompoundCrs | None = field(
        default=None,
        metadata={
            "name": "CompoundCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geocentric_crs: GeocentricCrs | None = field(
        default=None,
        metadata={
            "name": "GeocentricCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geographic_crs: GeographicCrs | None = field(
        default=None,
        metadata={
            "name": "GeographicCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    temporal_crs: TemporalCrs | None = field(
        default=None,
        metadata={
            "name": "TemporalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    image_crs: ImageCrs | None = field(
        default=None,
        metadata={
            "name": "ImageCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    engineering_crs: EngineeringCrs | None = field(
        default=None,
        metadata={
            "name": "EngineeringCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    vertical_crs: VerticalCrs | None = field(
        default=None,
        metadata={
            "name": "VerticalCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    geodetic_crs: GeodeticCrs | None = field(
        default=None,
        metadata={
            "name": "GeodeticCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derived_crs: DerivedCrs | None = field(
        default=None,
        metadata={
            "name": "DerivedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    projected_crs: ProjectedCrs | None = field(
        default=None,
        metadata={
            "name": "ProjectedCRS",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    conventional_unit: ConventionalUnit | None = field(
        default=None,
        metadata={
            "name": "ConventionalUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    derived_unit: DerivedUnit | None = field(
        default=None,
        metadata={
            "name": "DerivedUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    base_unit: BaseUnit | None = field(
        default=None,
        metadata={
            "name": "BaseUnit",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    unit_definition: UnitDefinition | None = field(
        default=None,
        metadata={
            "name": "UnitDefinition",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dictionary: Dictionary | None = field(
        default=None,
        metadata={
            "name": "Dictionary",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    definition: Definition | None = field(
        default=None,
        metadata={
            "name": "Definition",
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
    nil_reason: str | NilReasonEnumerationValue | None = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        },
    )
    remote_schema: str | None = field(
        default=None,
        metadata={
            "name": "remoteSchema",
            "type": "Attribute",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class DefinitionMember(DictionaryEntryType):
    class Meta:
        name = "definitionMember"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DictionaryEntry(DictionaryEntryType):
    """This property element contains or refers to the definitions which are
    members of a dictionary.

    The content model follows the standard GML property pattern, so a
    gml:dictionaryEntry may either contain or refer to a single
    gml:Definition. Since gml:Dictionary is substitutable for
    gml:Definition, the content of an entry may itself be a lower level
    dictionary. Note that if the value is provided by reference, this
    definition does not carry a handle (gml:id) in this context, so does
    not allow external references to this specific definition in this
    context.  When used in this way the referenced definition will
    usually be in a dictionary in the same XML document.
    """

    class Meta:
        name = "dictionaryEntry"
        namespace = "http://www.opengis.net/gml/3.2"
