from dataclasses import dataclass

from georama.maps.interfaces.iso.tc211.gmd.dataclasses.abstract_time_primitive_type import (
    AbstractTimeTopologyPrimitiveType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class AbstractTimeTopologyPrimitive(AbstractTimeTopologyPrimitiveType):
    """Gml:TimeTopologyPrimitive acts as the head of a substitution group for
    topological temporal primitives.

    Temporal topology primitives shall imply the ordering information
    between features or feature properties. The temporal connection of
    features can be examined if they have temporal topology primitives
    as values of their properties. Usually, an instantaneous feature
    associates with a time node, and a static feature associates with a
    time edge.  A feature with both modes associates with the temporal
    topology primitive: a supertype of time nodes and time edges. A
    topological primitive is always connected to one or more other
    topological primitives, and is, therefore, always a member of a
    topological complex. In a GML instance, this will often be indicated
    by the primitives being described by elements that are descendents
    of an element describing a complex. However, in order to support the
    case where a temporal topological primitive is described in another
    context, the optional complex property is provided, which carries a
    reference to the parent temporal topological complex.
    """

    class Meta:
        namespace = "http://www.opengis.net/gml"
