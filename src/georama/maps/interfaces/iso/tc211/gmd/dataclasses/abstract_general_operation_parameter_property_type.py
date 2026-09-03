from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_general_operation_parameter_type import (
    AbstractGeneralOperationParameterType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.maximum_occurs import (
    MaximumOccurs,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.operation_parameter_1 import (
    OperationParameter1,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue

__NAMESPACE__ = "http://www.opengis.net/gml"


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
            "namespace": "http://www.opengis.net/gml",
        },
    )
    operation_parameter: OperationParameter1 | None = field(
        default=None,
        metadata={
            "name": "OperationParameter",
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
        },
    )
    arcrole: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    title: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: ShowValue | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: ActuateValue | None = field(
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
            "namespace": "http://www.opengis.net/gml",
        },
    )


@dataclass
class GeneralOperationParameter(AbstractGeneralOperationParameterPropertyType):
    """
    Gml:generalOperationParameter is an association to an operation parameter or
    parameter group.
    """

    class Meta:
        name = "generalOperationParameter"
        namespace = "http://www.opengis.net/gml"


@dataclass
class UsesParameter(AbstractGeneralOperationParameterPropertyType):
    class Meta:
        name = "usesParameter"
        namespace = "http://www.opengis.net/gml"


@dataclass
class OperationParameterGroupType(AbstractGeneralOperationParameterType):
    maximum_occurs: MaximumOccurs | None = field(
        default=None,
        metadata={
            "name": "maximumOccurs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    uses_parameter: list[UsesParameter] = field(
        default_factory=list,
        metadata={
            "name": "usesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    general_operation_parameter: list[GeneralOperationParameter] = field(
        default_factory=list,
        metadata={
            "name": "generalOperationParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
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
        namespace = "http://www.opengis.net/gml"
