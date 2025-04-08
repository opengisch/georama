from dataclasses import dataclass, field
from typing import List, Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_parameter_value_type import (
    AbstractGeneralParameterValueType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.group import Group
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.parameter_value_1 import (
    ParameterValue1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.values_of_group import (
    ValuesOfGroup,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


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


@dataclass
class IncludesValue(AbstractGeneralParameterValuePropertyType):
    class Meta:
        name = "includesValue"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ParameterValue2(AbstractGeneralParameterValuePropertyType):
    """
    Gml:parameterValue is a composition association to a parameter value or group
    of parameter values used by a coordinate operation.
    """

    class Meta:
        name = "parameterValue"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesValue(AbstractGeneralParameterValuePropertyType):
    class Meta:
        name = "usesValue"
        namespace = "http://www.opengis.net/gml"


@dataclass
class ParameterValueGroupType(AbstractGeneralParameterValueType):
    includes_value: List[IncludesValue] = field(
        default_factory=list,
        metadata={
            "name": "includesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    uses_value: List[UsesValue] = field(
        default_factory=list,
        metadata={
            "name": "usesValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    parameter_value: List[ParameterValue2] = field(
        default_factory=list,
        metadata={
            "name": "parameterValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    values_of_group: Optional[ValuesOfGroup] = field(
        default=None,
        metadata={
            "name": "valuesOfGroup",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    group: Optional[Group] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
        namespace = "http://www.opengis.net/gml"
