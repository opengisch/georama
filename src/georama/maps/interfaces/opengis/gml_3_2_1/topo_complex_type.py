from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_topology_type import (
    AbstractTopologyType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.topo_primitive_member import (
    TopoPrimitiveMember,
)
from georama.maps.interfaces.opengis.gml_3_2_1.topo_primitive_members import (
    TopoPrimitiveMembers,
)
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoComplexType(AbstractTopologyType):
    maximal_complex: Optional["MaximalComplex"] = field(
        default=None,
        metadata={
            "name": "maximalComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "required": True,
        },
    )
    super_complex: list["SuperComplex"] = field(
        default_factory=list,
        metadata={
            "name": "superComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    sub_complex: list["SubComplex"] = field(
        default_factory=list,
        metadata={
            "name": "subComplex",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    topo_primitive_member: list[TopoPrimitiveMember] = field(
        default_factory=list,
        metadata={
            "name": "topoPrimitiveMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    topo_primitive_members: TopoPrimitiveMembers | None = field(
        default=None,
        metadata={
            "name": "topoPrimitiveMembers",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    is_maximal: bool = field(
        default=False,
        metadata={
            "name": "isMaximal",
            "type": "Attribute",
        },
    )
    aggregation_type: AggregationType | None = field(
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
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoComplexPropertyType:
    topo_complex: TopoComplex | None = field(
        default=None,
        metadata={
            "name": "TopoComplex",
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
class MaximalComplex(TopoComplexPropertyType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """

    class Meta:
        name = "maximalComplex"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SubComplex(TopoComplexPropertyType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """

    class Meta:
        name = "subComplex"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class SuperComplex(TopoComplexPropertyType):
    """
    The property elements gml:subComplex, gml:superComplex and gml:maximalComplex
    provide an encoding for relationships between topology complexes as described
    for gml:TopoComplex above.
    """

    class Meta:
        name = "superComplex"
        namespace = "http://www.opengis.net/gml/3.2"
