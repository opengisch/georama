from dataclasses import dataclass, field
from typing import Optional

from georama.maps.interfaces.opengis.gml_3_2_1.abstract_topo_primitive_type import (
    AbstractTopoPrimitiveType,
)
from georama.maps.interfaces.opengis.gml_3_2_1.actuate_type import ActuateType
from georama.maps.interfaces.opengis.gml_3_2_1.aggregation_type import AggregationType
from georama.maps.interfaces.opengis.gml_3_2_1.curve_property import CurveProperty
from georama.maps.interfaces.opengis.gml_3_2_1.nil_reason_enumeration_value import (
    NilReasonEnumerationValue,
)
from georama.maps.interfaces.opengis.gml_3_2_1.point_property import PointProperty
from georama.maps.interfaces.opengis.gml_3_2_1.show_type import ShowType
from georama.maps.interfaces.opengis.gml_3_2_1.sign_type import SignType
from georama.maps.interfaces.opengis.gml_3_2_1.solid_property import SolidProperty
from georama.maps.interfaces.opengis.gml_3_2_1.surface_property import SurfaceProperty
from georama.maps.interfaces.opengis.gml_3_2_1.type_type import TypeType

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class FaceOrTopoSolidPropertyType:
    face: Optional["Face"] = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    topo_solid: Optional["TopoSolid"] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class NodeOrEdgePropertyType:
    node: Optional["Node"] = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    edge: Optional["Edge"] = field(
        default=None,
        metadata={
            "name": "Edge",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class NodePropertyType:
    node: Optional["Node"] = field(
        default=None,
        metadata={
            "name": "Node",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TopoSolidPropertyType:
    topo_solid: Optional["TopoSolid"] = field(
        default=None,
        metadata={
            "name": "TopoSolid",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class NodeType(AbstractTopoPrimitiveType):
    """
    :ivar container:
    :ivar directed_edge: In the case of planar topology, a gml:Node must
        have a clockwise sequence of gml:directedEdge properties, to
        ensure a lossless topology representation as defined by
        Kuijpers, et. al. (see OGC 05-102 Topology IPR).
    :ivar point_property:
    :ivar aggregation_type:
    """

    container: FaceOrTopoSolidPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_edge: list["DirectedEdge"] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    point_property: PointProperty | None = field(
        default=None,
        metadata={
            "name": "pointProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class Node(NodeType):
    """Gml:Node represents the 0-dimensional primitive.

    The optional coboundary of a node (gml:directedEdge) is a sequence
    of directed edges which are incident on this node. Edges emanating
    from this node appear in the node coboundary with a negative
    orientation. If provided, the aggregationType attribute shall have
    the value "sequence". A node may optionally be realised by a
    0-dimensional geometric primitive (gml:pointProperty).
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectedNodePropertyType:
    node: Node | None = field(
        default=None,
        metadata={
            "name": "Node",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientation: SignType = field(
        default=SignType.PLUS_SIGN,
        metadata={
            "type": "Attribute",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DirectedNode(DirectedNodePropertyType):
    """A gml:directedNode property element describes the boundary of topology edges
    and is used in the support of topological point features via the gml:TopoPoint
    expression, see below.

    The orientation attribute of type gml:SignType expresses the sense
    in which the included node is used: start ("-") or end ("+") node.
    """

    class Meta:
        name = "directedNode"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class EdgeType(AbstractTopoPrimitiveType):
    container: TopoSolidPropertyType | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_node: list[DirectedNode] = field(
        default_factory=list,
        metadata={
            "name": "directedNode",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    directed_face: list["DirectedFace"] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    curve_property: CurveProperty | None = field(
        default=None,
        metadata={
            "name": "curveProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
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
class Edge(EdgeType):
    """Gml:Edge represents the 1-dimensional primitive.

    The topological boundary of an Edge (gml:directedNode) consists of a
    negatively directed start Node and a positively directed end Node.
    The optional coboundary of an edge (gml:directedFace) is a circular
    sequence of directed faces which are incident on this edge in
    document order. In the 2D case, the orientation of the face on the
    left of the edge is "+"; the orientation of the face on the right on
    its right is "-". If provided, the aggregationType attribute shall
    have the value "sequence". An edge may optionally be realised by a
    1-dimensional geometric primitive (gml:curveProperty).
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectedEdgePropertyType:
    edge: Edge | None = field(
        default=None,
        metadata={
            "name": "Edge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientation: SignType = field(
        default=SignType.PLUS_SIGN,
        metadata={
            "type": "Attribute",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DirectedEdge(DirectedEdgePropertyType):
    """A gml:directedEdge property element describes the boundary of topology
    faces, the coBoundary of topology nodes and is used in the support of
    topological line features via the gml:TopoCurve expression, see below.

    The orientation attribute of type gml:SignType expresses the sense
    in which the included edge is used, i.e. forward or reverse.
    """

    class Meta:
        name = "directedEdge"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class FaceType(AbstractTopoPrimitiveType):
    """
    :ivar isolated:
    :ivar directed_edge:
    :ivar directed_topo_solid:
    :ivar surface_property:
    :ivar aggregation_type:
    :ivar universal: If the topological representation exists an
        unbounded manifold (e.g. Euclidean plane), a gml:Face must
        indicate whether it is a universal face or not, to ensure a
        lossless topology representation as defined by Kuijpers, et. al.
        (see OGC 05-102 Topology IPR). The optional universal attribute
        of type boolean is used to indicate this. NOTE The universal
        face is normally not part of any feature, and is used to
        represent the unbounded portion of the data set. Its interior
        boundary (it has no exterior boundary) would normally be
        considered the exterior boundary of the map represented by the
        data set.
    """

    isolated: list[NodePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_edge: list[DirectedEdge] = field(
        default_factory=list,
        metadata={
            "name": "directedEdge",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    directed_topo_solid: list["DirectedTopoSolid"] = field(
        default_factory=list,
        metadata={
            "name": "directedTopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "max_occurs": 2,
        },
    )
    surface_property: SurfaceProperty | None = field(
        default=None,
        metadata={
            "name": "surfaceProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    aggregation_type: AggregationType | None = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
    universal: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Face(FaceType):
    """Gml:Face represents the 2-dimensional topology primitive.

    The topological boundary of a face (gml:directedEdge) consists of a
    sequence of directed edges. If provided, the aggregationType
    attribute shall have the value "sequence". The optional coboundary
    of a face (gml:directedTopoSolid) is a pair of directed solids which
    are bounded by this face. A positively directed solid corresponds to
    a solid which lies in the direction of the negatively directed
    normal to the face in any geometric realisation. A face may
    optionally be realised by a 2-dimensional geometric primitive
    (gml:surfaceProperty).
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectedFacePropertyType:
    face: Face | None = field(
        default=None,
        metadata={
            "name": "Face",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientation: SignType = field(
        default=SignType.PLUS_SIGN,
        metadata={
            "type": "Attribute",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DirectedFace(DirectedFacePropertyType):
    """The gml:directedFace property element describes the boundary of topology
    solids, in the coBoundary of topology edges and is used in the support of
    surface features via the gml:TopoSurface expression, see below.

    The orientation attribute of type gml:SignType expresses the sense
    in which the included face is used i.e. inward or outward with
    respect to the surface normal in any geometric realisation.
    """

    class Meta:
        name = "directedFace"
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class TopoSolidType(AbstractTopoPrimitiveType):
    """
    :ivar isolated:
    :ivar directed_face:
    :ivar solid_property:
    :ivar aggregation_type:
    :ivar universal: A gml:TopoSolid must indicate whether it is a
        universal topo-solid or not, to ensure a lossless topology
        representation as defined by Kuijpers, et. al. (see OGC 05-102
        Topology IPR). The optional universal attribute of type boolean
        is used to indicate this and the default is fault. NOTE The
        universal topo-solid is normally not part of any feature, and is
        used to represent the unbounded portion of the data set. Its
        interior boundary (it has no exterior boundary) would normally
        be considered the exterior boundary of the data set.
    """

    isolated: list[NodeOrEdgePropertyType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    directed_face: list[DirectedFace] = field(
        default_factory=list,
        metadata={
            "name": "directedFace",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
            "min_occurs": 1,
        },
    )
    solid_property: SolidProperty | None = field(
        default=None,
        metadata={
            "name": "solidProperty",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    aggregation_type: AggregationType | None = field(
        default=None,
        metadata={
            "name": "aggregationType",
            "type": "Attribute",
        },
    )
    universal: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class TopoSolid(TopoSolidType):
    """Gml:TopoSolid represents the 3-dimensional topology primitive.

    The topological boundary of a solid (gml:directedFace) consists of a
    set of directed faces. A solid may optionally be realised by a
    3-dimensional geometric primitive (gml:solidProperty).
    """

    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"


@dataclass
class DirectedTopoSolidPropertyType:
    topo_solid: TopoSolid | None = field(
        default=None,
        metadata={
            "name": "TopoSolid",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml/3.2",
        },
    )
    orientation: SignType = field(
        default=SignType.PLUS_SIGN,
        metadata={
            "type": "Attribute",
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
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class DirectedTopoSolid(DirectedTopoSolidPropertyType):
    """The gml:directedSolid property element describes the coBoundary of topology
    faces and is used in the support of volume features via the gml:TopoVolume
    expression, see below.

    The orientation attribute of type gml:SignType expresses the sense
    in which the included solid appears in the face coboundary. In the
    context of a gml:TopoVolume the orientation attribute has no
    meaning.
    """

    class Meta:
        name = "directedTopoSolid"
        namespace = "http://www.opengis.net/gml/3.2"
