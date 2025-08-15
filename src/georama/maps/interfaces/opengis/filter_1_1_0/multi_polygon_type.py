from dataclasses import dataclass, field

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)
from georama.maps.interfaces.opengis.filter_1_1_0.polygon_member import PolygonMember

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPolygonType(AbstractGeometricAggregateType):
    """A MultiPolygon is defined by one or more Polygons, referenced through
    polygonMember elements.

    Deprecated with GML version 3.0. Use MultiSurfaceType instead.
    """

    polygon_member: list[PolygonMember] = field(
        default_factory=list,
        metadata={
            "name": "polygonMember",
            "type": "Element",
            "namespace": "http://www.opengis.net/gml",
        },
    )
