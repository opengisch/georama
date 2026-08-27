from dataclasses import dataclass, field

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_parameter_value_type import (
    AbstractGeneralParameterValueType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.boolean_value import BooleanValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.dms_angle_value import (
    DmsAngleValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.integer_value import IntegerValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.integer_value_list import (
    IntegerValueList,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_parameter_2 import (
    OperationParameter2,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.string_value import StringValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.value import Value
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.value_file import ValueFile
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.value_list import ValueList
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.value_of_parameter import (
    ValueOfParameter,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ParameterValueType(AbstractGeneralParameterValueType):
    value: Value | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    dms_angle_value: DmsAngleValue | None = field(
        default=None,
        metadata={
            "name": "dmsAngleValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    string_value: StringValue | None = field(
        default=None,
        metadata={
            "name": "stringValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    integer_value: IntegerValue | None = field(
        default=None,
        metadata={
            "name": "integerValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    boolean_value: BooleanValue | None = field(
        default=None,
        metadata={
            "name": "booleanValue",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_list: ValueList | None = field(
        default=None,
        metadata={
            "name": "valueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    integer_value_list: IntegerValueList | None = field(
        default=None,
        metadata={
            "name": "integerValueList",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_file: ValueFile | None = field(
        default=None,
        metadata={
            "name": "valueFile",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    value_of_parameter: ValueOfParameter | None = field(
        default=None,
        metadata={
            "name": "valueOfParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter: OperationParameter2 | None = field(
        default=None,
        metadata={
            "name": "operationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
