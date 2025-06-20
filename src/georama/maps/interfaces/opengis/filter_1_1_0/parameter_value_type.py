from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_general_parameter_value_type import (
    AbstractGeneralParameterValueType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.boolean_value import BooleanValue
from georama.maps.interfaces.opengis.filter_1_1_0.dms_angle_value import DmsAngleValue
from georama.maps.interfaces.opengis.filter_1_1_0.integer_value import IntegerValue
from georama.maps.interfaces.opengis.filter_1_1_0.integer_value_list import (
    IntegerValueList,
)
from georama.maps.interfaces.opengis.filter_1_1_0.string_value import StringValue
from georama.maps.interfaces.opengis.filter_1_1_0.value import Value
from georama.maps.interfaces.opengis.filter_1_1_0.value_file import ValueFile
from georama.maps.interfaces.opengis.filter_1_1_0.value_list import ValueList
from georama.maps.interfaces.opengis.filter_1_1_0.value_of_parameter import (
    ValueOfParameter,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParameterValueType(AbstractGeneralParameterValueType):
    """A parameter value, ordered sequence of values, or reference to a file of
    parameter values.

    This concrete complexType can be used for operation methods without
    using an Application Schema that defines operation-method-
    specialized element names and contents, especially for methods with
    only one instance. This complexType can be used, extended, or
    restricted for well-known operation methods, especially for methods
    with many instances.
    """

    value: Optional[Value] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dms_angle_value: Optional[DmsAngleValue] = field(
        default=None,
        metadata={
            "name": "dmsAngleValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    string_value: Optional[StringValue] = field(
        default=None,
        metadata={
            "name": "stringValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    integer_value: Optional[IntegerValue] = field(
        default=None,
        metadata={
            "name": "integerValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_value: Optional[BooleanValue] = field(
        default=None,
        metadata={
            "name": "booleanValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_list: Optional[ValueList] = field(
        default=None,
        metadata={
            "name": "valueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    integer_value_list: Optional[IntegerValueList] = field(
        default=None,
        metadata={
            "name": "integerValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_file: Optional[ValueFile] = field(
        default=None,
        metadata={
            "name": "valueFile",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_of_parameter: Optional[ValueOfParameter] = field(
        default=None,
        metadata={
            "name": "valueOfParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
