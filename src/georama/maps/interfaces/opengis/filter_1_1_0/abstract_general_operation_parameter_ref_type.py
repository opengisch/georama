from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from georama.maps.interfaces.opengis.filter_1_1_0.actuate_type import ActuateType
from georama.maps.interfaces.opengis.filter_1_1_0.group_id import GroupId
from georama.maps.interfaces.opengis.filter_1_1_0.maximum_occurs import MaximumOccurs
from georama.maps.interfaces.opengis.filter_1_1_0.operation_parameter import (
    OperationParameter,
)
from georama.maps.interfaces.opengis.filter_1_1_0.operation_parameter_group_base_type import (
    OperationParameterGroupBaseType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.remarks import Remarks
from georama.maps.interfaces.opengis.filter_1_1_0.show_type import ShowType
from georama.maps.interfaces.opengis.filter_1_1_0.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractGeneralOperationParameterRefType:
    """
    Association to an operation parameter or group, either referencing or
    containing the definition of that parameter or group.
    """

    operation_parameter_group_or_operation_parameter: Optional[
        Union["OperationParameterGroup", OperationParameter]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperationParameterGroup",
                    "type": ForwardRef("OperationParameterGroup"),
                    "namespace": "http://www.opengis.net/gml",
                },
                {
                    "name": "OperationParameter",
                    "type": OperationParameter,
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
            "min_length": 1,
        },
    )
    arcrole: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
            "min_length": 1,
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    show: Optional[ShowType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
        },
    )
    actuate: Optional[ActuateType] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/1999/xlink",
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
class IncludesParameter(AbstractGeneralOperationParameterRefType):
    """
    Association to an operation parameter that is a member of a group.
    """

    class Meta:
        name = "includesParameter"
        namespace = "http://www.opengis.net/gml"


@dataclass
class OperationParameterGroupType(OperationParameterGroupBaseType):
    """The definition of a group of parameters used by an operation method.

    This complexType is expected to be used or extended for all
    applicable operation methods, without defining operation-method-
    specialized element names.

    :ivar group_id: Set of alternative identifications of this operation
        parameter group. The first groupID, if any, is normally the
        primary identification code, and any others are aliases.
    :ivar remarks: Comments on or information about this operation
        parameter group, including source information.
    :ivar maximum_occurs:
    :ivar includes_parameter: Unordered list of associations to the set
        of operation parameters that are members of this group.
    """

    group_id: list[GroupId] = field(
        default_factory=list,
        metadata={
            "name": "groupID",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    remarks: Optional[Remarks] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    maximum_occurs: Optional[MaximumOccurs] = field(
        default=None,
        metadata={
            "name": "maximumOccurs",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    includes_parameter: list[IncludesParameter] = field(
        default_factory=list,
        metadata={
            "name": "includesParameter",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "min_occurs": 2,
        },
    )


@dataclass
class OperationParameterGroup(OperationParameterGroupType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
