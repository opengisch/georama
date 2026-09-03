from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_general_parameter_value_type import (
    AbstractGeneralParameterValueType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.boolean_value import BooleanValue
from georama.maps.interfaces.opengis.gml_3_2_1.dms_angle_value import DmsAngleValue
from georama.maps.interfaces.opengis.gml_3_2_1.integer_value import IntegerValue
from georama.maps.interfaces.opengis.gml_3_2_1.integer_value_list import (
    IntegerValueList,
)
from georama.maps.interfaces.opengis.gml_3_2_1.operation_parameter_2 import (
    OperationParameter2,
)
from georama.maps.interfaces.opengis.gml_3_2_1.string_value import StringValue
from georama.maps.interfaces.opengis.gml_3_2_1.value import Value
from georama.maps.interfaces.opengis.gml_3_2_1.value_file import ValueFile
from georama.maps.interfaces.opengis.gml_3_2_1.value_list import ValueList
from georama.maps.interfaces.opengis.gml_3_2_1.value_of_parameter import (
    ValueOfParameter,
)

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class ParameterValueType(AbstractGeneralParameterValueType):
    value: Value | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    dms_angle_value: DmsAngleValue | None = field(
        default=None,
        metadata={
            "name": "dmsAngleValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    string_value: StringValue | None = field(
        default=None,
        metadata={
            "name": "stringValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    integer_value: IntegerValue | None = field(
        default=None,
        metadata={
            "name": "integerValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    boolean_value: BooleanValue | None = field(
        default=None,
        metadata={
            "name": "booleanValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    value_list: ValueList | None = field(
        default=None,
        metadata={
            "name": "valueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    integer_value_list: IntegerValueList | None = field(
        default=None,
        metadata={
            "name": "integerValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    value_file: ValueFile | None = field(
        default=None,
        metadata={
            "name": "valueFile",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    value_of_parameter: ValueOfParameter | None = field(
        default=None,
        metadata={
            "name": "valueOfParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    operation_parameter: OperationParameter2 | None = field(
        default=None,
        metadata={
            "name": "operationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
