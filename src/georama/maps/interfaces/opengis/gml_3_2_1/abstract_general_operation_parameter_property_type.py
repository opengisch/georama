from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_general_operation_parameter_type import (
    AbstractGeneralOperationParameterType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.maximum_occurs import MaximumOccurs
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.operation_parameter_1 import (
    OperationParameter1,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractGeneralOperationParameterPropertyType:
    """
    Gml:AbstractGeneralOperationParameterPropertyType is a property type for
    association roles to an operation parameter or group, either referencing or
    containing the definition of that parameter or group.
    """

    operation_parameter_group: Optional["OperationParameterGroup"] = field(
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
class GeneralOperationParameter(AbstractGeneralOperationParameterPropertyType):
    class Meta:
        name = "generalOperationParameter"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class IncludesParameter(AbstractGeneralOperationParameterPropertyType):
    class Meta:
        name = "includesParameter"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class Parameter(AbstractGeneralOperationParameterPropertyType):
    """
    Gml:parameter is an association to an operation parameter or parameter group.
    """

    class Meta:
        name = "parameter"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class UsesParameter(AbstractGeneralOperationParameterPropertyType):
    class Meta:
        name = "usesParameter"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class OperationParameterGroupType(AbstractGeneralOperationParameterType):
    maximum_occurs: MaximumOccurs | None = field(
        default=None,
        metadata={
            "name": "maximumOccurs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    uses_parameter: list[UsesParameter] = field(
        default_factory=list,
        metadata={
            "name": "usesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    general_operation_parameter: list[GeneralOperationParameter] = field(
        default_factory=list,
        metadata={
            "name": "generalOperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    includes_parameter: list[IncludesParameter] = field(
        default_factory=list,
        metadata={
            "name": "includesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    parameter: list[Parameter] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )


@dataclass
class OperationParameterGroup(OperationParameterGroupType):
    """Gml:OperationParameterGroup is the definition of a group of parameters used
    by an operation method.

    This complex type is expected to be used or extended for all
    applicable operation methods, without defining operation-method-
    specialized element names. The generalOperationParameter elements
    are an unordered list of associations to the set of operation
    parameters that are members of this group.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
