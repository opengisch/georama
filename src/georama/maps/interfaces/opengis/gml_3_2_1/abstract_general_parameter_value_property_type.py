from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_general_parameter_value_type import (
    AbstractGeneralParameterValueType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.group import Group
from georama.maps.interfaces.opengis.gml_3_2_1.parameter_value_1 import ParameterValue1
from georama.maps.interfaces.opengis.gml_3_2_1.values_of_group import ValuesOfGroup

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralParameterValuePropertyType:
    """
    Gml:AbstractGeneralParameterValuePropertyType is a  property type for inline
    association roles to a parameter value or group of parameter values, always
    containing the values.
    """

    parameter_value_group: Optional["ParameterValueGroup"] = field(
        default=None,
        metadata={
            "name": "ParameterValueGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    parameter_value: Optional[ParameterValue1] = field(
        default=None,
        metadata={
            "name": "ParameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class IncludesValue(AbstractGeneralParameterValuePropertyType):
    class Meta:
        name = "includesValue"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ParameterValue2(AbstractGeneralParameterValuePropertyType):
    """
    Gml:parameterValue is a composition association to a parameter value or group
    of parameter values used by a coordinate operation.
    """

    class Meta:
        name = "parameterValue"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesValue(AbstractGeneralParameterValuePropertyType):
    class Meta:
        name = "usesValue"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class ParameterValueGroupType(AbstractGeneralParameterValueType):
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
    values_of_group: Optional[ValuesOfGroup] = field(
        default=None,
        metadata={
            "name": "valuesOfGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    group: Optional[Group] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class ParameterValueGroup(ParameterValueGroupType):
    """Gml:ParameterValueGroup is a group of related parameter values.

    The same group can be repeated more than once in a Conversion,
    Transformation, or higher level ParameterValueGroup, if those
    instances contain different values of one or more parameterValues
    which suitably distinquish among those groups. This concrete complex
    type can be used for operation methods without using an Application
    Schema that defines operation-method-specialized element names and
    contents. This complex type may be used, extended, or restricted for
    well-known operation methods, especially for methods with only one
    instance. The parameterValue elements are an unordered set of
    composition association roles to the parameter values and groups of
    values included in this group.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
