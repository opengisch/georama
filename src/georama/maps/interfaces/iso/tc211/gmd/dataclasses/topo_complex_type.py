from dataclasses import dataclass, field
from typing import List, Optional, Union

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_topology_type import (
    AbstractTopologyType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.actuate_value import ActuateValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.aggregation_type import (
    AggregationType,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.show_value import ShowValue
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.topo_primitive_member import (
    TopoPrimitiveMember,
)
from georama.maps.interfaces.iso.tc211.gmd.dataclasses.topo_primitive_members import (
    TopoPrimitiveMembers,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class TopoComplexType(AbstractTopologyType):
    maximal_complex: Optional["MaximalComplex"] = field(
        default=None,
        metadata={
            "name": "maximalComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
            "required": True,
        },
    )
    super_complex: List["SuperComplex"] = field(
        default_factory=list,
        metadata={
            "name": "superComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    sub_complex: List["SubComplex"] = field(
        default_factory=list,
        metadata={
            "name": "subComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_primitive_member: List[TopoPrimitiveMember] = field(
        default_factory=list,
        metadata={
            "name": "topoPrimitiveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    topo_primitive_members: Optional[TopoPrimitiveMembers] = field(
        default=None,
        metadata={
            "name": "topoPrimitiveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
    is_maximal: bool = field(
        default=False,
        metadata={
            "name": "isMaximal",
            "type": "Attribute",
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
class TopoComplex(TopoComplexType):
    """Gml:TopoComplex is a collection of topological primitives.

    Each complex holds a reference to its maximal complex
    (gml:maximalComplex) and optionally to sub- or super-complexes
    (gml:subComplex, gml:superComplex). A topology complex contains its
    primitive and sub-complex members.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"


@dataclass
class TopoComplexMemberType:
    topo_complex: Optional[TopoComplex] = field(
        default=None,
        metadata={
            "name": "TopoComplex",
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
class MaximalComplex(TopoComplexMemberType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """

    class Meta:
        name = "maximalComplex"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SubComplex(TopoComplexMemberType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """

    class Meta:
        name = "subComplex"
        namespace = "http://www.opengis.net/gml"


@dataclass
class SuperComplex(TopoComplexMemberType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """

    class Meta:
        name = "superComplex"
        namespace = "http://www.opengis.net/gml"
