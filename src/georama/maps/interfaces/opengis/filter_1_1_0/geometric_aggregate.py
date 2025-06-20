from dataclasses import dataclass

from georama.maps.interfaces.opengis.filter_1_1_0.abstract_geometric_aggregate_type import (
    AbstractGeometricAggregateType,
)

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometricAggregate(AbstractGeometricAggregateType):
    """
    The "_GeometricAggregate" element is the abstract head of the substituition
    group for all geometric aggremates.
    """

    class Meta:
        name = "_GeometricAggregate"
        namespace = "http://www.opengis.net/gml"
