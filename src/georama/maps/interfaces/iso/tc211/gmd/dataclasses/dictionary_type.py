from dataclasses import dataclass, field
from typing import List, Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_operation_parameter_property_type import (
    OperationParameterGroup,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_member_type import (
    AbstractMemberType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.affine_cs_1 import AffineCs1
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.aggregation_type import (
    AggregationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.base_unit import BaseUnit
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cartesian_cs_1 import (
    CartesianCs1,
)
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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.cylindrical_cs import (
    CylindricalCs,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition import Definition
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_proxy import (
    DefinitionProxy,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.definition_type import (
    DefinitionType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.derived_unit import DerivedUnit
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ellipsoid_1 import Ellipsoid1
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.ellipsoidal_cs_1 import (
    EllipsoidalCs1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.indirect_entry import (
    IndirectEntry,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.linear_cs import LinearCs
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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.polar_cs import PolarCs
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.prime_meridian_1 import (
    PrimeMeridian1,
)
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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.spherical_cs_1 import (
    SphericalCs1,
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
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.transformation import (
    Transformation,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.unit_definition import (
    UnitDefinition,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.user_defined_cs import (
    UserDefinedCs,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.vertical_cs_1 import VerticalCs1

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DictionaryType(DefinitionType):
    definition_member: List["DefinitionMember"] = field(
        default_factory=list,
        metadata={
            "name": "definitionMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dictionary_entry: List["DictionaryEntry"] = field(
        default_factory=list,
        metadata={
            "name": "dictionaryEntry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    indirect_entry: List[IndirectEntry] = field(
        default_factory=list,
        metadata={
            "name": "indirectEntry",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
class DefinitionCollection(DictionaryType):
    class Meta:
        namespace = "http://www.opengis.net/gml"


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
        namespace = "http://www.opengis.net/gml"


@dataclass
class DictionaryEntryType(AbstractMemberType):
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
class DefinitionMember(DictionaryEntryType):
    class Meta:
        name = "definitionMember"
        namespace = "http://www.opengis.net/gml"


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
        namespace = "http://www.opengis.net/gml"
